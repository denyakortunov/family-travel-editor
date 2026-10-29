import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skills/family-travel-editor/scripts'))
sys.path.insert(0, str(ROOT / 'tools'))
from project import catalog, doctor
from install_skill import install


class CatalogRecovery(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / 'media folder'
        self.source.mkdir()
        self.output = self.root / 'catalog.json'

    def tearDown(self):
        self.temp.cleanup()

    def test_timeout_keeps_earlier_and_later_records(self):
        for name in ('a.mp4', 'b.mp4', 'c.mp4'):
            (self.source / name).write_bytes(b'fixture')
        ok = subprocess.CompletedProcess([], 0, '{"streams": [{"codec_type": "video"}]}', '')
        with patch('project.shutil.which', return_value='/fake/ffprobe'), patch(
                'project.subprocess.run', side_effect=[ok, subprocess.TimeoutExpired('ffprobe', 120), ok]), redirect_stderr(io.StringIO()) as progress:
            self.assertEqual(catalog(self.source, self.output), 3)
        data = json.loads(self.output.read_text())
        self.assertEqual([r['metadata_status'] for r in data['files']], ['probed', 'failed', 'probed'])
        self.assertEqual(data['summary']['failed'], 1)
        self.assertIn('timed out', data['files'][1]['error'])
        self.assertIn('[3/3]', progress.getvalue())
        self.assertTrue(all('sha256' in r for r in data['files']))

    def test_invalid_probe_and_unreadable_file_do_not_abort(self):
        for name in ('a.mp4', 'b.mp4', 'c.mp4'):
            (self.source / name).write_bytes(b'fixture')
        with patch('project.shutil.which', return_value='/fake/ffprobe'), patch(
                'project.sha256', side_effect=['abc', OSError('cannot read file'), 'def']), patch(
                'project.subprocess.run', side_effect=[subprocess.CompletedProcess([], 0, 'not json', ''),
                subprocess.CompletedProcess([], 0, '{}', '')]), redirect_stderr(io.StringIO()):
            self.assertEqual(catalog(self.source, self.output), 3)
        data = json.loads(self.output.read_text())
        self.assertEqual(data['summary']['failed'], 3)
        self.assertNotIn('sha256', data['files'][1])

    def test_skipped_files_and_empty_cli_are_actionable(self):
        (self.source / 'notes.txt').write_text('sidecar')
        result = subprocess.run([sys.executable, str(ROOT / 'skills/family-travel-editor/scripts/project.py'),
            'catalog', str(self.source), '--output', str(self.output)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('No media candidates', result.stderr)
        data = json.loads(self.output.read_text())
        self.assertEqual(data['summary']['included'], 0)
        self.assertEqual(data['skipped'][0]['path'], 'notes.txt')
        self.assertIn('extension', data['skipped'][0]['reason'])

    def test_candidate_extensions_are_case_insensitive_not_codec_certification(self):
        for name in ('clip.MTS', 'clip.webm', 'clip.mxf', 'audio.flac'):
            (self.source / name).write_bytes(b'not playable')
        with patch('project.shutil.which', return_value=None), redirect_stderr(io.StringIO()):
            self.assertEqual(catalog(self.source, self.output), 4)
        data = json.loads(self.output.read_text())
        self.assertEqual(data['summary']['metadata_unavailable'], 4)
        self.assertEqual(data['summary']['failed'], 0)

    def test_unreadable_directory_is_reported_as_partial(self):
        (self.source / 'visible.mp4').write_bytes(b'fixture')
        hidden = self.source / 'unreadable'
        hidden.mkdir()
        (hidden / 'missing.mp4').write_bytes(b'fixture')
        hidden.chmod(0)
        try:
            if os.access(hidden, os.R_OK):
                self.skipTest('This user can read directories despite mode 000')
            result = subprocess.run([sys.executable, str(ROOT / 'skills/family-travel-editor/scripts/project.py'),
                'catalog', str(self.source), '--output', str(self.output), '--ffprobe', 'missing-probe'],
                capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            data = json.loads(self.output.read_text())
            self.assertEqual(data['summary']['included'], 1)
            self.assertEqual(data['summary']['scan_failed'], 1)
            self.assertEqual(data['scan_errors'][0]['path'], 'unreadable')
            self.assertIn('coverage is incomplete', result.stderr)
        finally:
            hidden.chmod(0o700)

    def test_doctor_missing_and_existing_source(self):
        self.assertTrue(doctor(source=self.source)['ready'])
        report = doctor(source=self.root / 'missing')
        self.assertFalse(report['ready'])
        self.assertFalse(report['source']['readable_directory'])
        self.assertFalse((self.root / 'missing').exists())

    def test_relative_install_returns_absolute_paths(self):
        previous = Path.cwd()
        try:
            os.chdir(self.root)
            target, backup = install(ROOT / 'skills/family-travel-editor', Path('agent folder/skills'))
            self.assertTrue(target.is_absolute())
            target, backup = install(ROOT / 'skills/family-travel-editor', Path('agent folder/skills'), update=True)
            self.assertTrue(backup.is_absolute())
            self.assertTrue((backup / 'SKILL.md').is_file())
        finally:
            os.chdir(previous)
