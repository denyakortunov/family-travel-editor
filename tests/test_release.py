import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]


class ReleaseInstall(unittest.TestCase):
    def test_both_archives_are_self_contained(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            output = root / 'packages'
            subprocess.run([sys.executable, str(ROOT / 'tools/package_release.py'),
                            '--output', str(output)], check=True, capture_output=True)
            sums = dict(line.split('  ', 1)[::-1] for line in (output / 'SHA256SUMS.txt').read_text().splitlines())
            for kind in ('source', 'plugin'):
                version = json.loads((ROOT / 'plugin.json').read_text())['version']
                archive = output / f'family-travel-editor-{kind}-v{version}.zip'
                self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), sums[archive.name])
                extracted = root / kind
                with zipfile.ZipFile(archive) as package:
                    self.assertFalse(any('__pycache__' in n or '/.git/' in n for n in package.namelist()))
                    package.extractall(extracted)
                package_root = extracted / 'family-travel-editor' if kind == 'source' else extracted
                skill = package_root / 'skills/family-travel-editor'
                self.assertEqual((skill / 'VERSION').read_text().strip(), version)
                result = subprocess.run([sys.executable, str(skill / 'scripts/self_test.py')],
                                        cwd=root, check=True, capture_output=True, text=True)
                self.assertIn('PASS:', result.stdout)
                if kind == 'source':
                    installed = root / 'installed-skills'
                    subprocess.run([sys.executable, str(package_root / 'tools/install_skill.py'),
                                    '--destination', str(installed)], check=True, capture_output=True)
                    subprocess.run([sys.executable, str(installed / 'family-travel-editor/scripts/self_test.py')],
                                   cwd=root, check=True, capture_output=True)

class ReleasePublication(unittest.TestCase):
    def setUp(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location('publisher', ROOT / 'tools/publish_release.py')
        self.publisher = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.publisher)

    def test_api_failure_stops_without_publication(self):
        from unittest.mock import patch
        with patch.dict('os.environ', {'GH_REPO': 'example/repo', 'GITHUB_SHA': 'a' * 40}), \
             patch.object(self.publisher.subprocess, 'run', side_effect=subprocess.CalledProcessError(1, 'gh')) as call:
            with self.assertRaises(subprocess.CalledProcessError):
                self.publisher.run()
            self.assertEqual(call.call_count, 1)

    def test_existing_release_is_untouched(self):
        from unittest.mock import patch
        version = json.loads((ROOT / 'plugin.json').read_text())['version']
        with patch.dict('os.environ', {'GH_REPO': 'example/repo', 'GITHUB_SHA': 'a' * 40}), \
             patch.object(self.publisher.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, f'v{version}\n')) as call:
            self.publisher.run()
            self.assertEqual(call.call_count, 1)

    def test_publishes_exact_tested_commit_and_assets(self):
        from unittest.mock import patch
        actual_run = subprocess.run
        observed = []
        def fake_run(command, **kwargs):
            observed.append(command)
            if command[0] == sys.executable:
                return actual_run(command, **kwargs)
            return subprocess.CompletedProcess(command, 0, '')
        with patch.dict('os.environ', {'GH_REPO': 'example/repo', 'GITHUB_SHA': 'a' * 40}), \
             patch.object(self.publisher.subprocess, 'run', side_effect=fake_run):
            self.publisher.run()
        create = observed[-1]
        self.assertEqual(create[:3], ['gh', 'release', 'create'])
        self.assertEqual(create[create.index('--target') + 1], 'a' * 40)
        self.assertEqual(sum(value.endswith('.zip') for value in create), 2)
        self.assertEqual(sum(value.endswith('SHA256SUMS.txt') for value in create), 1)
