#!/usr/bin/env python3
"""Copy the skill into a chosen discovery directory; never overwrite a skill."""
import argparse
from pathlib import Path
import shutil

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--destination', type=Path, required=True)
a = p.parse_args()
source = Path(__file__).resolve().parents[1] / 'skills/family-travel-editor'
target = a.destination.expanduser() / source.name
if target.exists() or target.is_symlink():
    p.exit(1, f'Refusing to replace existing skill: {target}\n')
target.parent.mkdir(parents=True, exist_ok=True)
shutil.copytree(source, target, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
print(f'Installed {target}. Start a fresh chat to refresh skill discovery.')
