import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / 'examples/grand-canyon-sunset'
spec = importlib.util.spec_from_file_location('real_demo', EXAMPLE / 'run_demo.py')
real_demo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(real_demo)


class ExamplePrerequisites(unittest.TestCase):
    def test_results_cannot_be_written_inside_example(self):
        target = EXAMPLE / 'media' / 'must-not-be-created'
        with self.assertRaisesRegex(ValueError, 'outside the supplied example'):
            real_demo.run(target)
        self.assertFalse(target.exists())

    def test_missing_tools_leave_no_output(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / 'new'
            with self.assertRaisesRegex(ValueError, 'FFmpeg and ffprobe'):
                real_demo.run(out, ffmpeg='missing-ffmpeg-for-test')
            self.assertFalse(out.exists())

    def test_existing_workspace_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            (out / 'my-notes.txt').write_text('keep me')
            with self.assertRaises(FileExistsError):
                real_demo.run(out)
            self.assertEqual((out / 'my-notes.txt').read_text(), 'keep me')


@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'Media tests need FFmpeg and ffprobe')
class RealFootageExample(unittest.TestCase):
    def test_real_sources_and_bounded_revision(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / 'Проба сцены'
            subprocess.run([sys.executable, str(EXAMPLE / 'run_demo.py'), '--output', str(out)],
                           check=True, capture_output=True)
            for version, frames in [('v1',600),('v2',550)]:
                info = json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames',
                    '-show_streams','-of','json',str(out / (version+'.mp4'))],text=True))
                self.assertEqual([s['codec_type'] for s in info['streams']], ['video'])
                self.assertEqual(info['streams'][0]['nb_read_frames'], str(frames))
            a=json.loads((EXAMPLE/'v1.json').read_text());b=json.loads((EXAMPLE/'v2.json').read_text())
            self.assertEqual(a['shots'][:2],b['shots'][:2])
            self.assertEqual(a['shots'][2]['out'],b['shots'][2]['out'])
            self.assertEqual(b['shots'][2]['in']-a['shots'][2]['in'],50)
            self.assertTrue((out/'verification.json').is_file())
            self.assertTrue((out/'STATUS.md').is_file())
            self.assertEqual(json.loads((out/'v2.json').read_text()),b)
            self.assertIn(str(out), (out/'STATUS.md').read_text())
            self.assertFalse(list(out.glob('.preview-*')))
