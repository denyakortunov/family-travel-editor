#!/usr/bin/env python3
"""Render a silent straight-cut preview; never modify originals or overwrite outputs."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
from timeline import validate
from media_checks import check_sources


def render(plan, media_root, output, ffmpeg='ffmpeg', ffprobe='ffprobe'):
    root = validate(plan, media_root)
    output = Path(output).resolve()
    if output.exists() or output.is_symlink():
        raise FileExistsError(output)
    if root in output.parents:
        raise ValueError('Write previews outside the source media directory')
    if output.suffix.lower() != '.mp4':
        raise ValueError('Preview output must be .mp4')
    encoder, probe = shutil.which(ffmpeg), shutil.which(ffprobe)
    if not encoder or not probe:
        raise ValueError('FFmpeg and ffprobe are required; supply --ffmpeg PATH and --ffprobe PATH')
    check_sources(plan, root, probe)
    output.parent.mkdir(parents=True, exist_ok=True)
    command = [encoder, '-v', 'error', '-nostdin', '-n', '-xerror']
    for shot in plan['shots']:
        command += ['-i', str(root / shot['path'])]
    filters = [f'[{i}:v:0]trim=start_frame={s["in"]}:end_frame={s["out"]},setpts=PTS-STARTPTS,setsar=1[v{i}]'
               for i, s in enumerate(plan['shots'])]
    filters.append(''.join(f'[v{i}]' for i in range(len(plan['shots']))) +
                   f'concat=n={len(plan["shots"])}:v=1:a=0[out]')
    expected = sum(s['out'] - s['in'] for s in plan['shots'])
    # Do not expose a partial failed render as the requested deliverable.
    with tempfile.TemporaryDirectory(prefix='.preview-', dir=output.parent) as temp:
        staged = Path(temp) / 'preview.mp4'
        subprocess.run(command + ['-filter_complex', ';'.join(filters), '-map', '[out]',
            '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', str(plan['fps']), '-fps_mode', 'cfr',
            '-an', '-movflags', '+faststart', str(staged)], check=True)
        result = subprocess.run([probe, '-v', 'error', '-select_streams', 'v:0', '-count_frames',
            '-show_entries', 'stream=nb_read_frames', '-of', 'json', str(staged)],
            check=True, capture_output=True, text=True)
        actual = int(json.loads(result.stdout)['streams'][0]['nb_read_frames'])
        if result.stderr.strip() or actual != expected:
            raise ValueError(f'Preview verification failed: expected {expected}, got {actual} frames')
        with output.open('xb') as dest, staged.open('rb') as source:
            shutil.copyfileobj(source, dest)
    return expected


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('plan', type=Path); p.add_argument('--media-root', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--ffmpeg', default='ffmpeg'); p.add_argument('--ffprobe', default='ffprobe')
    a = p.parse_args()
    try:
        frames = render(json.loads(a.plan.read_text()), a.media_root, a.output, a.ffmpeg, a.ffprobe)
        print(f'Wrote {frames} video frames. SILENT preview: no dialogue, music or native editor project.')
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        p.exit(1, f'Error: {error}\n')


if __name__ == '__main__':
    main()
