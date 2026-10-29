#!/usr/bin/env python3
"""Publish a previously unshipped version after CI; never replace an existing release."""
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


def run():
    root = Path(__file__).resolve().parents[1]
    version = json.loads((root / 'plugin.json').read_text())['version']
    if not re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', version):
        raise ValueError('Expected a numeric major.minor.patch version')
    if (root / 'skills/family-travel-editor/VERSION').read_text().strip() != version:
        raise ValueError('Plugin and skill versions differ')
    notes = root / f'docs/whats-new-v{version}.md'
    if not notes.is_file():
        raise ValueError(f'Missing release notes: {notes.name}')
    tag = f'v{version}'
    # A failed API read stops the run; never interpret an auth/network failure as no release.
    response = subprocess.run(['gh', 'api', '--paginate', f'repos/{os.environ["GH_REPO"]}/releases',
                               '--jq', '.[].tag_name'], check=True, capture_output=True, text=True)
    if tag in response.stdout.splitlines():
        print(f'{tag} already published; leaving it unchanged.')
        return
    with tempfile.TemporaryDirectory(prefix='family-travel-release-') as temp:
        output = Path(temp) / 'packages'
        subprocess.run([sys.executable, str(root / 'tools/package_release.py'), '--output', str(output)], check=True)
        # Never move an existing tag or guess what its intended release should contain.
        tags = subprocess.run(['gh', 'api', '--paginate', f'repos/{os.environ["GH_REPO"]}/tags',
                               '--jq', '.[].name'], check=True, capture_output=True, text=True)
        if tag in tags.stdout.splitlines():
            raise ValueError(f'{tag} already exists without a release; inspect it before publishing')
        subprocess.run(['gh', 'release', 'create', tag, '--target', os.environ['GITHUB_SHA'],
                        '--title', f'{tag} — Family Travel Editor', '--notes-file', str(notes), '--latest',
                        *[str(p) for p in sorted(output.iterdir())]], check=True)


if __name__ == '__main__':
    run()
