#!/usr/bin/env python3
"""Optional: download verified NPS originals and prepare separate silent copies."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import urllib.request


def prepare(output, ffmpeg='ffmpeg'):
    example = Path(__file__).resolve().parent
    output = Path(output).expanduser().resolve()
    if output.exists():
        raise FileExistsError('Choose a new directory; existing files are never replaced.')
    encoder = shutil.which(ffmpeg)
    if not encoder:
        raise ValueError('FFmpeg is required; pass --ffmpeg PATH or install it first.')
    output.mkdir(parents=True)
    originals = output / 'originals'; originals.mkdir()
    media = output / 'media'; media.mkdir()
    downloaded = {}
    for source in json.loads((example / 'sources.json').read_text())['sources']:
        target = originals / (source['id'] + '.mp4')
        print('Downloading official NPS source: ' + source['id'], flush=True)
        req = urllib.request.Request(source['download'], headers={'User-Agent': 'FamilyTravelEditor-example'})
        with urllib.request.urlopen(req, timeout=60) as response, target.open('xb') as destination:
            while True:
                block = response.read(1024 * 1024)
                if not block:
                    break
                destination.write(block)
                if destination.tell() > 50 * 1024 * 1024:
                    raise ValueError('Download exceeded the expected small source size; inspect the source URL.')
        if hashlib.sha256(target.read_bytes()).hexdigest() != source['sha256']:
            raise ValueError('Downloaded source changed: ' + source['id'] + '. Stop and inspect the official source; do not update hashes blindly.')
        downloaded[source['id']] = target
    manifest = json.loads((example / 'media-manifest.json').read_text())
    for item in manifest:
        target = media / item['file']
        subprocess.run([encoder, '-hide_banner', '-loglevel', 'error', '-nostdin', '-n',
            '-ss', str(item['source_in_seconds']), '-i', str(downloaded[item['source_id']]),
            '-frames:v', str(item['frames']), '-map', '0:v:0',
            '-vf', 'setpts=PTS-STARTPTS,fps=25:start_time=0,scale=640:360,setsar=1', '-c:v', 'libx264', '-preset', 'medium',
            '-crf', '21', '-pix_fmt', 'yuv420p', '-an', '-movflags', '+faststart', str(target)], check=True)
        item['sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
        item['bytes'] = target.stat().st_size
    (output / 'media-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Prepared separate silent copies at ' + str(media))
    print('Encoded hashes can vary with FFmpeg versions. Originals were verified; playback speed was not changed.')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', required=True, type=Path)
    p.add_argument('--ffmpeg', default='ffmpeg')
    a = p.parse_args()
    try:
        prepare(a.output, a.ffmpeg)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        p.exit(1, f'Error: {error}\n')
