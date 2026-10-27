#!/usr/bin/env python3
"""Build a new editable Shotcut MLT project: one silent video track, straight cuts."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET
from timeline import validate
from media_checks import check_sources


def prop(parent, name, value):
    ET.SubElement(parent, 'property', name=name).text = str(value)


def build(plan, media_root, output, ffprobe='ffprobe'):
    root = validate(plan, media_root)
    target = Path(output).expanduser()
    if target.exists() or target.is_symlink():
        raise FileExistsError(target)
    target = target.resolve()
    if root in target.parents:
        raise ValueError('Write the project outside the source media directory')
    if target.suffix.lower() != '.mlt':
        raise ValueError('Shotcut project output must be .mlt')
    sources = check_sources(plan, root, ffprobe)
    duration = sum(s['out'] - s['in'] for s in plan['shots'])
    aspect = Fraction(plan['width'], plan['height'])
    xml = ET.Element('mlt', LC_NUMERIC='C', producer='tractor', version='7.24.0')
    ET.SubElement(xml, 'profile', description=plan.get('name', 'Travel scene'),
        width=str(plan['width']), height=str(plan['height']), frame_rate_num=str(plan['fps']),
        frame_rate_den='1', progressive='1', sample_aspect_num='1', sample_aspect_den='1',
        display_aspect_num=str(aspect.numerator), display_aspect_den=str(aspect.denominator), colorspace='709')
    black = ET.SubElement(xml, 'producer', id='black', **{'in': '0', 'out': str(duration - 1)})
    for key, value in [('resource', '0'), ('mlt_service', 'color'), ('mlt_image_format', 'rgba'),
                       ('length', duration), ('eof', 'pause'), ('set.test_audio', 1)]:
        prop(black, key, value)
    background = ET.SubElement(xml, 'playlist', id='background')
    ET.SubElement(background, 'entry', producer='black', **{'in': '0', 'out': str(duration - 1)})
    for i, shot in enumerate(plan['shots']):
        chain = ET.SubElement(xml, 'chain', id=f'clip{i}', **{'in': '0', 'out': str(shot['source_frames'] - 1)})
        for key, value in [('resource', str(root / shot['path'])), ('mlt_service', 'avformat'),
                           ('length', shot['source_frames']), ('eof', 'pause'), ('video_index', sources[root / shot['path']]['index']),
                           ('audio_index', -1), ('set.test_audio', 1), ('shotcut:producer', 1),
                           ('shotcut:caption', Path(shot['path']).name)]:
            prop(chain, key, value)
    media_bin = ET.SubElement(xml, 'playlist', id='main_bin')
    prop(media_bin, 'xml_retain', 1); prop(media_bin, 'shotcut:main_bin', 1)
    for i, shot in enumerate(plan['shots']):
        ET.SubElement(media_bin, 'entry', producer=f'clip{i}', **{'in': '0', 'out': str(shot['source_frames'] - 1)})
    track = ET.SubElement(xml, 'playlist', id='video')
    prop(track, 'shotcut:name', 'V1'); prop(track, 'shotcut:trackHeight', 64)
    for i, shot in enumerate(plan['shots']):
        # JSON out is exclusive; MLT out is inclusive. Convert exactly once.
        ET.SubElement(track, 'entry', producer=f'clip{i}', **{'in': str(shot['in']), 'out': str(shot['out'] - 1)})
    timeline = ET.SubElement(xml, 'tractor', id='tractor', shotcut='1', **{'in': '0', 'out': str(duration - 1)})
    prop(timeline, 'shotcut', 1); prop(timeline, 'shotcut:name', plan.get('name', 'Travel scene'))
    prop(timeline, 'shotcut:projectAudioChannels', 2)
    ET.SubElement(timeline, 'track', producer='background')
    ET.SubElement(timeline, 'track', producer='video', hide='audio')
    ET.indent(xml)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('xb') as stream:
        ET.ElementTree(xml).write(stream, encoding='utf-8', xml_declaration=True)
    return duration


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('plan', type=Path); p.add_argument('--media-root', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True); p.add_argument('--ffprobe', default='ffprobe')
    args = p.parse_args()
    try:
        count = build(json.loads(args.plan.read_text()), args.media_root, args.output, args.ffprobe)
        print(f'Wrote editable Shotcut project: {count} frames on V1. Source audio is MUTED; no music or titles.')
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        p.exit(1, f'Error: {error}\n')


if __name__ == '__main__':
    main()
