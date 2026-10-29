#!/usr/bin/env python3
"""Install the skill; explicit updates preserve a sibling backup."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import tempfile


def install(source, destination, update=False):
    source, destination = Path(source), Path(destination).expanduser()
    target = destination / source.name
    if target.is_symlink() or (target.exists() and not target.is_dir()):
        raise ValueError('Refusing to replace a symlink or non-directory skill')
    if target.exists() and not update:
        raise FileExistsError(f'{target}: use --update to preserve a backup and install the new version')
    destination.mkdir(parents=True, exist_ok=True)
    # Backups are outside the discovery directory to avoid duplicate skill discovery.
    backup = None
    with tempfile.TemporaryDirectory(prefix='.skill-stage-', dir=destination.parent) as staging:
        staged = Path(staging) / source.name
        shutil.copytree(source, staged, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        if target.exists():
            backups = destination.parent / (destination.name + '-backups')
            backups.mkdir(exist_ok=True)
            stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
            backup = backups / (source.name + '-' + stamp)
            target.rename(backup)
        try:
            staged.rename(target)
        except OSError:
            if backup is not None:
                backup.rename(target)
            raise
    return target, backup


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--destination', type=Path, required=True)
    p.add_argument('--update', action='store_true', help='Preserve the old skill in a sibling skills-backups directory')
    a = p.parse_args()
    try:
        target, backup = install(Path(__file__).resolve().parents[1] / 'skills/family-travel-editor', a.destination, a.update)
    except (OSError, ValueError) as error:
        p.exit(1, f'Error: {error}\n')
    version = (target / 'VERSION').read_text().strip()
    print(f'Installed family-travel-editor {version} at {target}.')
    print('Open a new chat and invoke $family-travel-editor. If absent, restart your agent.')
    print(f'Check installation: python3 "{target / "scripts/self_test.py"}"')
    print('Installing does not start an edit. Give the agent your footage folder and one scene.')
    if backup:
        print(f'Previous installation preserved: {backup}')


if __name__ == '__main__':
    main()
