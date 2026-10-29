#!/usr/bin/env python3
"""Run the bundled real-footage picture exercise into a new folder. No downloads."""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys


def run(output, ffmpeg='ffmpeg', ffprobe='ffprobe'):
    example = Path(__file__).resolve().parent
    repository = example.parents[1]
    scripts = repository / 'skills/family-travel-editor/scripts'
    output = Path(output).expanduser().resolve()
    if output == example or example in output.parents:
        raise ValueError('Keep results outside the supplied example folder to preserve its inputs.')
    if output.exists():
        raise FileExistsError('Choose a new output folder; existing work is never replaced.')
    for tool in (ffmpeg, ffprobe):
        if not shutil.which(tool):
            raise ValueError('This video exercise needs FFmpeg and ffprobe. Install them or pass --ffmpeg PATH --ffprobe PATH. Planning and self_test.py still work without them.')
    for item in json.loads((example / 'media-manifest.json').read_text()):
        path = example / 'media' / item['file']
        if hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            raise ValueError(f'Included source copy differs from its manifest: {item["file"]}; extract a fresh source archive.')
    output.mkdir(parents=True)
    def helper(name, *args):
        subprocess.run([sys.executable, str(scripts / name), *map(str, args)], check=True)
    helper('project.py', 'catalog', example / 'media', '--output', output / 'catalog.json', '--ffprobe', ffprobe)
    for version in ('v1', 'v2'):
        helper('timeline.py', example / (version + '.json'), '--media-root', example / 'media', '--output', output / (version + '.xml'))
        helper('render_preview.py', example / (version + '.json'), '--media-root', example / 'media', '--output', output / (version + '.mp4'), '--ffmpeg', ffmpeg, '--ffprobe', ffprobe)
    result = {'scope': 'Silent real-footage picture exercise; no native editor or audio conform',
              'expected_frames': {'v1': 600, 'v2': 550},
              'files': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in output.iterdir() if p.is_file()}}
    for name in ('scene.json', 'v1.json', 'v2.json', 'feedback.json', 'preferences.json'):
        shutil.copyfile(example / name, output / name)
    now = datetime.now().astimezone().isoformat(timespec='seconds')
    skill_version = (scripts.parent / 'VERSION').read_text().strip()
    status = f'''# Grand Canyon picture exercise — v2

Updated: {now}. Operator: run_demo.py using skill {skill_version}.
Workspace: {output}
Source copies: {example / 'media'} (unchanged). Keep this source folder in place; XML uses absolute media paths.
Current plan: v2.json; previous plan: v1.json. Both copied into this workspace.
Native editor project: none. Review outputs: v1.mp4 (600 frames / 24 s), v2.mp4 (550 frames / 22 s), both intentionally silent.
Export identities: verification.json.
Completed: catalogue, video-only XML and both helper renders; source hashes and output frame counts checked.
Not checked: native editor import/playback/export, original audio, artistic quality or author acceptance. No viewing/listening is claimed by running this script.
Feedback: the simulated request changes only the final IN from 50 to 100, keeping OUT 250 and earlier ranges.
Remaining: watch the actual outputs and record your judgement. A real film needs separate speech/music work.
Processes: none remain after this successful command.
Next: read scene.json, v1.json, v2.json, feedback.json, preferences.json and verification.json; compare both previews.
Required answer: none for this completed exercise.
Handoff: local files only, no synchronization claim.

Resume prompt: Read the installed SKILL.md, then this workspace's STATUS.md and linked plans/feedback/verification. Confirm the source folder is still accessible. Continue from v2 without replacing files, inventing author acceptance or calling XML a tested native project.
'''
    (output / 'STATUS.md').write_text(status)
    result['files'].update({p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in output.iterdir() if p.is_file()})
    (output / 'verification.json').write_text(json.dumps(result, indent=2) + '\n')
    print(f'Open {output / "v1.mp4"} and {output / "v2.mp4"}. Both are intentionally SILENT.')
    print('v1: 24 seconds; v2: 22 seconds. The first two shots are unchanged; the last starts two seconds later.')
    print(f'Resume in a fresh chat by asking the agent to read {output / "STATUS.md"}.')
    print('XML is video-only interchange, not proof of a working native editor project.')
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', required=True, type=Path)
    p.add_argument('--ffmpeg', default='ffmpeg')
    p.add_argument('--ffprobe', default='ffprobe')
    a = p.parse_args()
    try:
        run(a.output, a.ffmpeg, a.ffprobe)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        p.exit(1, f'Error: {error}\n')


if __name__ == '__main__':
    main()
