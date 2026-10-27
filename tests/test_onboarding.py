import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skills/family-travel-editor/scripts'))
sys.path.insert(0, str(ROOT / 'tools'))
from project import doctor
from timeline import validate
from render_preview import render
from install_skill import install


class Onboarding(unittest.TestCase):
    def test_planning_without_external_tools(self):
        with patch('project.shutil.which', return_value=None):
            self.assertTrue(doctor('plan')['ready'])
            self.assertTrue(doctor('catalog')['ready'])
            self.assertFalse(doctor('preview')['ready'])
            self.assertEqual(doctor('preview')['missing'], ['ffmpeg', 'ffprobe'])
            self.assertIsNone(doctor('resolve')['ready'])

    def test_narrative_rejected_with_next_step(self):
        with self.assertRaisesRegex(ValueError, 'shot-plan-v1.json'):
            validate({'title': 'Arrival', 'shots': []}, '.')
        for malformed in [[], None, {'fps': 25, 'width': 640, 'height': 360, 'shots': [None]}]:
            with self.assertRaises(ValueError):
                validate(malformed, '.')

    def test_install_update_preserves_local_copy(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); source = root / 'source' / 'demo'; source.mkdir(parents=True)
            (source / 'SKILL.md').write_text('version one')
            target, backup = install(source, root / 'skills')
            self.assertIsNone(backup)
            (target / 'notes.txt').write_text('local notes')
            with self.assertRaises(FileExistsError):
                install(source, root / 'skills')
            (source / 'SKILL.md').write_text('version two')
            target, backup = install(source, root / 'skills', update=True)
            self.assertEqual((target / 'SKILL.md').read_text(), 'version two')
            self.assertEqual((backup / 'SKILL.md').read_text(), 'version one')
            self.assertEqual((backup / 'notes.txt').read_text(), 'local notes')
            self.assertNotIn(root / 'skills', backup.parents)

    def test_clean_install_workspace_and_xml(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            target, _ = install(ROOT / 'skills/family-travel-editor', root / 'skills')
            command = [sys.executable, str(target / 'scripts/project.py'), 'init', str(root / 'film')]
            subprocess.run(command, check=True, capture_output=True)
            self.assertEqual(set(p.name for p in (root / 'film').iterdir()),
                             {'STATUS.md', 'scene.json', 'feedback.json', 'preferences.json'})
            self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0)
            result = subprocess.run([sys.executable, str(target / 'scripts/timeline.py'),
                str(ROOT / 'examples/first-scene/generated/v2.json'), '--media-root',
                str(ROOT / 'examples/first-scene/generated/media'), '--output', str(root / 'v2.xml')],
                check=True, capture_output=True, text=True)
            self.assertIn('250 video frames', result.stdout)


@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'Media tests need FFmpeg and ffprobe')
class Preview(unittest.TestCase):
    def test_real_fixture_render_and_refusals(self):
        fixture = ROOT / 'examples/first-scene/generated'
        plan = json.loads((fixture / 'v2.json').read_text())
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / 'preview.mp4'
            self.assertEqual(render(plan, fixture / 'media', out), 250)
            result = subprocess.run(['ffprobe', '-v', 'error', '-show_streams', '-of', 'json', str(out)],
                                    check=True, capture_output=True, text=True)
            streams = json.loads(result.stdout)['streams']
            self.assertEqual([s['codec_type'] for s in streams], ['video'])
            self.assertEqual(streams[0]['nb_frames'], '250')
            with self.assertRaises(FileExistsError):
                render(plan, fixture / 'media', out)
            plan['shots'][0]['source_frames'] = 101
            with self.assertRaisesRegex(ValueError, 'does not match plan'):
                render(plan, fixture / 'media', Path(temp) / 'bad.mp4')
            self.assertFalse((Path(temp) / 'bad.mp4').exists())
            plan['shots'][0]['source_frames'] = 100
            plan['fps'] = 30
            with self.assertRaisesRegex(ValueError, 'does not match plan'):
                render(plan, fixture / 'media', Path(temp) / 'rate.mp4')
