# Agent trials, not human usability studies

The maintainer chose agent-based checks for now. No new human participants were recruited and no success rate for human newcomers is claimed.

## 29 October 2026: Claude Opus 5.5

An independent Claude Code session received the public skill, the Grand Canyon example and a first-use request: check the setup, run the example into a new folder with no chosen editor, explain the revision and provide a way to continue tomorrow. It was restricted to public inputs and separate test outputs; it did not change the repository or native editor.

What it actually did:

- Ran the planning/preview doctor and installation self-test.
- Rendered the 24-second and 22-second examples; checked the source files remained unchanged.
- Checked output hashes, decoded frame counts, absence of audio and video-only XML source ranges.
- Compared the protected frame intervals and the selected ending against a deliberately wrong range as a control.
- Inspected 14 still images. It did not watch uninterrupted motion or listen to the original sound.

Useful findings led to changes: the run now writes its own STATUS and copies the plans; helper messages no longer require Resolve or falsely advise installing ffprobe during a synthetic self-test; transient rendering files use the system temporary directory. The exercise documents absolute paths and the need to preserve/relink XML media paths. Release numbering was brought into sync before publication.

The first-run trial observed hidden staging videos in a cloud-synchronized result folder despite a completed command. The exact cause was not established; relocating staging avoids putting these transient files into the result folder in the first place.

## Fresh-session continuation

A second Claude Opus 5.5 session received only the saved workspace and skill. It verified the existing exports, source identities and plan/XML ranges without rerendering. The generated STATUS was sufficient to continue, no staging directories were present in that workspace, and the normal self-test passed without the earlier misleading warning. One attempted `python3 -I` invocation failed because isolation removes the script directory from imports; the documented normal invocation worked.

The reviewer confused original NPS downloads with the included silent derivatives in one narrative sentence. Original AAC streams were already verified; the sentence now names both categories explicitly. Workspace verification also records hashes of copied plans and status, not only exports.

## Local checks

Automated tests run the real-footage exercise in a fresh path containing spaces and non-Latin characters, check both frame counts and no-audio scope, preserve existing workspaces, reject writes into source folders, and verify that copied plans and STATUS support continuation. The broader suite covers catalogue recovery, installation/update backups, XML and packaging.

Source selection was inspected in timed frame sheets; the rendered versions were decoded and compared. Encoded bytes and some decoded pixels can differ through compression even when source ranges are preserved. A successful test is evidence of the stated checks, not artistic approval or native-editor compatibility.

## What remains outside these checks

Real human first-use behavior, native editor import/save/reopen/export, Windows end-to-end execution, dialogue/music work and a complete personal travel film are not established by this trial. The [picture example](../examples/grand-canyon-sunset/README.md) and [no-footage planning trial](../examples/memory-to-plan/README.md) deliberately state their different scopes.
