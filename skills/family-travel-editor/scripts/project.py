#!/usr/bin/env python3
"""Local project helpers. No network access or account credentials."""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

MEDIA = {'.mov', '.mp4', '.mkv', '.m4v', '.wav', '.mp3', '.m4a', '.jpg', '.jpeg', '.png', '.heic'}


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def save_new(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8') as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write('\n')


def catalog(source, output, ffprobe='ffprobe'):
    source, output = Path(source).resolve(), Path(output).resolve()
    if not source.is_dir():
        raise ValueError('Source must be a readable directory')
    if output == source or source in output.parents:
        raise ValueError('Write the catalogue outside the source directory')
    if output.exists():
        raise FileExistsError(output)
    executable = shutil.which(ffprobe)
    records = []
    for path in sorted(source.rglob('*')):
        if path.is_symlink() or not path.is_file() or path.suffix.lower() not in MEDIA:
            continue
        # Do not follow a symlinked source into an unrelated folder.
        if source not in path.resolve().parents:
            continue
        record = {'path': path.relative_to(source).as_posix(), 'bytes': path.stat().st_size,
                  'sha256': sha256(path), 'metadata_status': 'unavailable'}
        if executable:
            result = subprocess.run([executable, '-v', 'error', '-show_streams', '-show_format',
                                     '-of', 'json', str(path)], capture_output=True, text=True, timeout=120)
            if result.returncode == 0:
                record.update(metadata_status='probed', metadata=json.loads(result.stdout))
            else:
                record.update(metadata_status='failed', error=result.stderr[-2000:])
        records.append(record)
    save_new(output, {'schema_version': 1, 'files': records,
                      'note': 'Metadata and hashes only; content has not been watched or listened to.'})
    return len(records)


def measure(media, output, ffmpeg='ffmpeg'):
    media, output = Path(media).resolve(), Path(output).resolve()
    if not media.is_file():
        raise FileNotFoundError(media)
    if output.exists() or output == media:
        raise FileExistsError(output)
    executable = shutil.which(ffmpeg)
    if not executable:
        raise ValueError('FFmpeg is unavailable; supply --ffmpeg PATH')
    result = subprocess.run([executable, '-hide_banner', '-nostdin', '-xerror', '-i', str(media),
                             '-map', '0:v?', '-map', '0:a?', '-vf', 'blackdetect=d=0.5,freezedetect=d=2',
                             '-af', 'loudnorm=print_format=json', '-f', 'null', '-'],
                            capture_output=True, text=True)
    report = {'schema_version': 1, 'file': media.name, 'sha256': sha256(media),
              'decode_returncode': result.returncode,
              'status': 'measurement_completed' if result.returncode == 0 else 'measurement_failed',
              'ffmpeg_log': result.stderr,
              'limitations': ['Not a listening or editorial verdict.',
                              'Black/freeze flags need interpretation; no speech completeness check.',
                              'No stereo-correlation or mono-compatibility test is performed.']}
    save_new(output, report)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('doctor')
    init = sub.add_parser('init'); init.add_argument('workspace', type=Path)
    cat = sub.add_parser('catalog'); cat.add_argument('source', type=Path)
    cat.add_argument('--output', type=Path, required=True); cat.add_argument('--ffprobe', default='ffprobe')
    qc = sub.add_parser('measure'); qc.add_argument('media', type=Path)
    qc.add_argument('--output', type=Path, required=True); qc.add_argument('--ffmpeg', default='ffmpeg')
    args = parser.parse_args()
    try:
        if args.command == 'doctor':
            print(json.dumps({'python': sys.version.split()[0], 'platform': sys.platform,
                              'ffmpeg': shutil.which('ffmpeg'), 'ffprobe': shutil.which('ffprobe'),
                              'resolve': 'Run resolve_bridge.py probe separately; not checked.'}, indent=2))
        elif args.command == 'init':
            args.workspace.mkdir(parents=True, exist_ok=False)
            templates = Path(__file__).resolve().parents[1] / 'assets/templates'
            for item in templates.iterdir():
                shutil.copyfile(item, args.workspace / item.name)
            print('Created a new planning workspace.')
        elif args.command == 'catalog':
            print(f'Catalogued {catalog(args.source, args.output, args.ffprobe)} files.')
        elif args.command == 'measure':
            return measure(args.media, args.output, args.ffmpeg)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
