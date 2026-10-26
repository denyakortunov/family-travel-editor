# First scene: synthetic timing example

This example is deliberately synthetic: animated FFmpeg test patterns, no people, no speech, no music. It tests the technical loop, not the artistic claims of the workflow.

- [v1 preview](generated/v1.mp4): three four-second shots, 300 frames at 25 fps.
- [v2 preview](generated/v2.mp4): the middle shot is shortened to two seconds, 250 frames.
- [Feedback](generated/feedback.json): preserve the first and final shots.
- [Source clips](generated/media/) and explicit [v1](generated/v1.json) / [v2](generated/v2.json) plans.

From the repository root, with FFmpeg available:

```sh
python3 examples/first-scene/make_demo.py --output /path/to/new-demo
```

Use a directory that does not exist; the generator refuses to overwrite results. `--ffmpeg /path/to/ffmpeg` selects an existing binary. The output includes both preview videos and local `v1.xml` / `v2.xml` timelines. XML is intentionally regenerated locally because source media paths differ between machines.

To build XML from the checked-in plan and clips:

```sh
python3 skills/family-travel-editor/scripts/timeline.py examples/first-scene/generated/v2.json --media-root examples/first-scene/generated/media --output /path/to/new-v2.xml
```

Open a **new, empty** Resolve project named `Family Travel Editor Demo`, then import that XML using File → Import → Timeline or the guarded helper:

```sh
python3 skills/family-travel-editor/scripts/resolve_bridge.py import-xml /path/to/new-v2.xml --project 'Family Travel Editor Demo'
```

The helper refuses a different or populated project. Live import has not yet been validated for this release. Confirm source relinking, 25 fps, 250 video frames and actual rendered playback before treating it as successful. This XML has no audio tracks.

The checked-in preview was rendered with FFmpeg, not Resolve. It must not be presented as a verified Resolve export. [Validation coverage](../../docs/validation.md).
