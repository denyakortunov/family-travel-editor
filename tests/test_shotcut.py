import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skills/family-travel-editor/scripts'))
from shotcut import build
from render_preview import render


class ShotcutPlan(unittest.TestCase):
    def test_edit_ranges_and_paths(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); media = root / 'media'; media.mkdir()
            (media / 'a & b.mp4').write_bytes(b'fixture')
            plan = {'fps': 25, 'width': 640, 'height': 360,
                    'shots': [{'path': 'a & b.mp4', 'in': 25, 'out': 75, 'source_frames': 100}]}
            output = root / 'scene.mlt'
            with patch('shotcut.check_sources', return_value={(media / 'a & b.mp4').resolve(): {'index': 0}}):
                self.assertEqual(build(plan, media, output), 50)
                with self.assertRaises(FileExistsError): build(plan, media, output)
                with self.assertRaises(ValueError): build(plan, media, media / 'bad.mlt')
            tree = ET.parse(output)
            entry = tree.find("./playlist[@id='video']/entry")
            self.assertEqual((entry.get('in'), entry.get('out')), ('25', '74'))
            self.assertEqual(tree.find('./tractor').get('out'), '49')
            self.assertEqual(tree.findtext("./chain/property[@name='resource']"), str((media / 'a & b.mp4').resolve()))
            self.assertEqual(tree.find("./tractor/track[@producer='video']").get('hide'), 'audio')
            self.assertEqual(tree.findtext("./playlist[@id='main_bin']/property[@name='shotcut:main_bin']"), '1')

    def test_rejects_escape_before_probe(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); media = root / 'media'; media.mkdir()
            (root / 'outside.mp4').write_bytes(b'fixture')
            plan = {'fps': 25, 'width': 640, 'height': 360,
                    'shots': [{'path': '../outside.mp4', 'in': 0, 'out': 25, 'source_frames': 25}]}
            with patch('shotcut.check_sources') as probe:
                with self.assertRaises(ValueError): build(plan, media, root / 'bad.mlt')
                probe.assert_not_called()


@unittest.skipUnless(all(shutil.which(x) for x in ['melt', 'ffmpeg', 'ffprobe']),
                     'Native MLT tests require melt, FFmpeg and ffprobe')
class MeltRoundTrip(unittest.TestCase):
    def test_render_reload_and_cut_alignment(self):
        fixture = ROOT / 'examples/first-scene/generated'
        plan = json.loads((fixture / 'v2.json').read_text())
        plan['shots'][0]['in'] = 25  # Catch implementations that always start at frame zero.
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); project = root / 'scene.mlt'
            self.assertEqual(build(plan, fixture / 'media', project), 225)
            reference = root / 'reference.mp4'
            render(plan, fixture / 'media', reference)
            env = dict(os.environ, LC_ALL='C', QT_QPA_PLATFORM='offscreen')
            def melt(source, consumer, *options):
                return subprocess.run(['melt', str(source), '-consumer', consumer, *options],
                    env=env, check=True, capture_output=True, timeout=90)
            reloaded = root / 'reloaded.mlt'
            melt(project, 'xml:' + str(reloaded), 'store=shotcut')
            self.assertTrue(reloaded.is_file())
            # Generic MLT serialization tests the connected timeline; it is not a Shotcut UI save.
            # Detached media-bin retention is a separate Shotcut UI save check.
            tree = ET.parse(reloaded)
            self.assertTrue(tree.findall(".//property[@name='shotcut']"))
            def pixels(path):
                return subprocess.check_output(['ffmpeg', '-v', 'error', '-i', str(path),
                    '-vf', 'format=rgb24,scale=32:18:flags=area,format=rgb24', '-an', '-f', 'rawvideo', '-'])
            expected = pixels(reference)
            self.assertEqual(len(expected), 225 * 32 * 18 * 3)
            for name, source in [('original', project), ('reloaded', reloaded)]:
                output = root / (name + '.mp4')
                melt(source, 'avformat:' + str(output), 'vcodec=libx264', 'crf=18', 'an=1')
                streams = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-count_frames',
                    '-show_streams', '-of', 'json', str(output)]))['streams']
                self.assertEqual([s['codec_type'] for s in streams], ['video'])
                self.assertEqual(int(streams[0]['nb_read_frames']), 225)
                self.assertEqual(streams[0]['avg_frame_rate'], '25/1')
                actual = pixels(output)
                self.assertEqual(len(actual), len(expected))
                # Compare every frame, including the cut boundaries, at reduced resolution.
                errors = [sum(abs(a-b) for a,b in zip(actual[i:i+1728], expected[i:i+1728]))/1728
                          for i in range(0, len(actual), 1728)]
                worst = max(range(len(errors)), key=errors.__getitem__)
                print('MLT metrics:', name, streams[0]['width'], streams[0]['height'], 'worst frame', worst, 'errors', errors[::25], flush=True)
                self.assertEqual((streams[0]['width'], streams[0]['height']), (640, 360))
                self.assertLess(max(errors), 8.0, (name, worst, max(errors)))
