#!/usr/bin/env python3
"""Build clean source and plugin ZIPs without Git history or local workspaces."""
import argparse
import hashlib
from pathlib import Path
import zipfile

p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True)
a=p.parse_args();a.output.mkdir(parents=True,exist_ok=False)
root=Path(__file__).resolve().parents[1]
allowed=['README.md','README.ru.md','LICENSE','THIRD_PARTY_NOTICES.md','plugin.json','skills','docs','assets','examples','tests','tools','.github','.gitignore']
files=[]
for name in allowed:
 path=root/name
 for item in ([path] if path.is_file() else sorted(path.rglob('*'))):
  if item.is_file() and not item.is_symlink() and '__pycache__' not in item.parts and item.suffix!='.pyc':files.append(item)
for kind in ['source','plugin']:
 out=a.output/f'family-travel-editor-{kind}-v0.1.0.zip'
 with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED) as z:
  for item in files:
   rel=item.relative_to(root)
   if kind=='plugin' and rel.parts[0] not in ['plugin.json','skills','assets','LICENSE']:continue
   z.write(item,str(rel) if kind=='plugin' else 'family-travel-editor/'+str(rel))
checks=[]
for item in sorted(a.output.glob('*.zip')):checks.append(hashlib.sha256(item.read_bytes()).hexdigest()+'  '+item.name)
(a.output/'SHA256SUMS.txt').write_text('\n'.join(checks)+'\n')
print('\n'.join(checks))
