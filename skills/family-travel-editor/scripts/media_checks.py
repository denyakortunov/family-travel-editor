"""Shared source checks for the limited same-rate picture-only adapters."""
from fractions import Fraction
import json
import shutil
import subprocess


def check_sources(plan, root, ffprobe='ffprobe'):
    probe = shutil.which(ffprobe)
    if not probe:
        raise ValueError('ffprobe is required; supply --ffprobe PATH')
    # Decode/count each distinct input and reject unsupported normalization needs.
    checked = {}
    for shot in plan['shots']:
        path = root / shot['path']
        if path not in checked:
            result = subprocess.run([probe, '-v', 'error', '-select_streams', 'v:0',
                '-count_frames', '-show_streams', '-of', 'json', str(path)],
                check=True, capture_output=True, text=True)
            if result.stderr.strip():
                raise ValueError(f'Source probe reported errors: {shot["path"]}')
            streams = json.loads(result.stdout).get('streams', [])
            if not streams:
                raise ValueError(f'No video stream: {shot["path"]}')
            checked[path] = streams[0]
        stream = checked[path]
        try:
            matching = (Fraction(stream['avg_frame_rate']) == plan['fps'] == Fraction(stream['r_frame_rate'])
                        and stream['width'] == plan['width'] and stream['height'] == plan['height']
                        and int(stream['nb_read_frames']) == shot['source_frames'])
        except (KeyError, ValueError, ZeroDivisionError):
            matching = False
        rotated = any(float(s.get('rotation', 0)) % 360 for s in stream.get('side_data_list', []))
        rotated = rotated or float(stream.get('tags', {}).get('rotate', 0)) % 360
        square = stream.get('sample_aspect_ratio', '1:1') in ('1:1', '0:1', 'N/A')
        if not matching or rotated or not square:
            raise ValueError(f'Source does not match plan (rate, dimensions, frames, rotation or pixel aspect): {shot["path"]}. Normalize a separate copy first.')
    return checked
