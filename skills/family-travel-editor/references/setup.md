# Setup and commands

Start with Python 3.9+ and local access to the footage. Native editing targets DaVinci Resolve Studio on macOS; other installations are not validated. FFmpeg and ffprobe are separate tools: install them using a trusted package manager or your existing installation. No models, accounts or paid services are installed automatically.

From the skill directory:

```sh
python3 scripts/project.py doctor
python3 scripts/project.py init /absolute/path/to/new-workspace
python3 scripts/project.py catalog /absolute/path/to/footage --output /absolute/path/to/workspace/catalog.json
python3 scripts/project.py measure /absolute/path/to/export.mp4 --output /absolute/path/to/workspace/checks.json
python3 scripts/resolve_bridge.py probe
```

`catalog` lists media by relative path, size and SHA-256. If ffprobe is available it adds stream and duration metadata; otherwise metadata is explicitly unavailable. It does not inspect creative content, interpret dates, or transcribe. Reading full hashes can take time on large media. It ignores directory symlinks and rejects outputs inside the source tree.

`measure` requires FFmpeg; it decodes the complete video/audio, logs freeze/black and audio loudness analyses, and reports decode errors. Logs are observations requiring interpretation: black frames may be intentional, still scenery is not automatically an error, and silence has no finite integrated loudness. `--ffmpeg` / `--ffprobe` override executable names. The script never rewrites an export.

Without connected Photos/Gmail, use a user-selected metadata export and questions. Without Replay, use a table of version + timecode + comment. Without audio models, use available measurements and human listening, with coverage disclosed. Cloud audio analysis requires the user's authorized service and material transfer; names in the diagram do not mean those services are bundled.
