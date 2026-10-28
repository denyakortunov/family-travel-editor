# Shotcut / MLT: experimental picture-only adapter

The adapter writes a new `.mlt` project with a source bin and three or more individually editable clip entries (one clip is also valid). It uses the same shot-plan JSON as the FFmpeg preview and Resolve XML helpers. It never edits an existing Shotcut project. Desktop opening, editing and saving are a separate validation step from command-line MLT rendering; check the current validation record in the source repository (`docs/validation.md`).

## Build one scene

From the repository root:

```sh
python3 skills/family-travel-editor/scripts/shotcut.py examples/first-scene/generated/v2.json --media-root examples/first-scene/generated/media --output /path/to/new-scene.mlt
```

From an installed skill, use `scripts/shotcut.py` with your own plan and footage root. Supply `--ffprobe PATH` if ffprobe is not on PATH. Shotcut bundles ffprobe; on macOS an ordinary installation provides `/Applications/Shotcut.app/Contents/MacOS/ffprobe`. Use the actual installed location.

Requirements: Python 3.9+, ffprobe, actual constant-rate 24/25/30 fps sources matching the plan dimensions, unrotated square pixels. Read [plan formats](plan-formats.md) before selecting ranges. The script checks metadata and frame counts but does not certify arbitrary variable-frame-rate media. Normalize a separate copy when needed.

**Source sound is deliberately muted.** This first adapter is a picture-only assembly: no dialogue conform, audio mix, transitions, titles, effects, HDR/color-management workflow or existing-project revisions. Do not use it as a finished family-film exporter. Save the original sound separately for later work.

## Open and verify in Shotcut

Open the generated `.mlt`. Confirm the profile, source relinking, V1 clips and cut points. For the included v2 fixture expect 25 fps and 250 frames: 100 + 50 + 100. Scrub around frames 99/100 and 149/150; all three shots must be present. Save As a new version, close/reopen it and confirm the clips remain editable. Verify the actual export as well. Do not replace a production project to test this adapter.

Source paths are absolute local paths. Moving the project to another computer requires regenerating against the new media root or relinking in Shotcut. Keep the plan with the film workspace; do not commit your private paths or footage to a public repository.

## Render without driving the UI

Shotcut's documented command-line renderer is MLT `melt`. The example below intentionally exports no audio. Choose a fresh output filename: unlike our Python helpers, a direct `melt` command can overwrite an existing output.

```sh
LC_ALL=C melt /path/to/new-scene.mlt -consumer avformat:/path/to/new-preview.mp4 vcodec=libx264 crf=18 an=1 movflags=+faststart
```

On macOS use the actual bundled executable, commonly `/Applications/Shotcut.app/Contents/MacOS/melt`. Linux distributions may package `melt` separately. Do not assume the command is on PATH just because the editor is installed.

A generic MLT XML load/serialize/render cycle proves the connected timeline's cut timing. It does not prove Shotcut's desktop save preserves the detached media bin and application-specific UI state. Report these checks separately.

Official references: [Shotcut command-line export](https://forum.shotcut.org/t/export-at-the-command-line/44067), [MLT XML](https://www.mltframework.org/docs/mltxml/), [MLT XML serialization](https://www.mltframework.org/plugins/ConsumerXml/).
