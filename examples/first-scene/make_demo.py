#!/usr/bin/env python3
"""Generate redistributable synthetic clips and a before/after timing example."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'skills/family-travel-editor/scripts'))
from timeline import build


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--ffmpeg', default='ffmpeg')
    a = p.parse_args()
    ffmpeg = shutil.which(a.ffmpeg)
    if not ffmpeg:
        p.exit(1, 'FFmpeg is required. Supply --ffmpeg PATH.\n')
    a.output.mkdir(parents=True, exist_ok=False)
    media = a.output / 'media'; media.mkdir()
    for i in range(1, 4):
        subprocess.run([ffmpeg, '-v', 'error', '-nostdin', '-n', '-f', 'lavfi', '-i',
                        'testsrc2=size=640x360:rate=25:duration=4', '-vf', f'hue=h={i*70}',
                        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-an',
                        str(media / f'shot-{i}.mp4')], check=True)
    v1 = {'name': 'Synthetic scene v1', 'fps': 25, 'width': 640, 'height': 360,
          'shots': [{'path': f'shot-{i}.mp4', 'in': 0, 'out': 100, 'source_frames': 100,
                     'role': role} for i, role in enumerate(['establish', 'action', 'result'], 1)]}
    v2 = json.loads(json.dumps(v1)); v2['name'] = 'Synthetic scene v2'; v2['shots'][1]['out'] = 50
    for version, plan in [('v1', v1), ('v2', v2)]:
        (a.output / f'{version}.json').write_text(json.dumps(plan, indent=2)+'\n')
        build(plan, media, a.output / f'{version}.xml')
        command = [ffmpeg, '-v', 'error', '-nostdin', '-n']
        for shot in plan['shots']:
            command += ['-i', str(media / shot['path'])]
        chains = [f'[{i}:v]trim=start_frame={s["in"]}:end_frame={s["out"]},setpts=PTS-STARTPTS[v{i}]'
                  for i, s in enumerate(plan['shots'])]
        chains += ['[v0][v1][v2]concat=n=3:v=1:a=0[out]']
        command += ['-filter_complex', ';'.join(chains), '-map', '[out]', '-c:v', 'libx264',
                    '-pix_fmt', 'yuv420p', '-r', str(plan['fps']), '-fps_mode', 'cfr', '-an', str(a.output / f'{version}.mp4')]
        subprocess.run(command, check=True)
    (a.output / 'feedback.json').write_text(json.dumps({'synthetic': True, 'comments': [
        {'id': 'demo-1', 'version': 'v1', 'timecode': '00:00:04:00',
         'request': 'Shorten the middle shot by two seconds; preserve the first and last shots.',
         'status': 'applied', 'result_version': 'v2', 'verification': 'See validation.md; no author acceptance claimed.'}]}, indent=2)+'\n')
    print('Generated synthetic video-only example: v1 = 300 frames; v2 = 250 frames at 25 fps.')
    print('XML contains local media paths. Regenerate after moving the example.')


if __name__ == '__main__':
    main()
