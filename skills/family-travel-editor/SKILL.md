---
name: family-travel-editor
description: Plan and edit family travel films from existing footage in DaVinci Resolve, reconstruct trip context, draft personal narration, and apply timecoded feedback while preserving the editable project.
---

# Family Travel Editor

Turn a collection of clips into a coherent film with the filmmaker. Work on one named scene or revision at a time; keep an editable timeline and evidence of what was checked. This skill needs local file access for media operations and a working Resolve installation for native editing. Installing it does not install Resolve, grant account access, or supply audio models.

## Start from the actual project

Find the user's workspace, current project/version, footage and preferences. Continue existing work when present. For a new project, use `scripts/project.py init WORKSPACE` to create empty planning files. Do not initialize over an existing project. Select a short representative scene before scaling to a whole trip.

Use `scripts/project.py doctor` for tool availability. Read [setup](references/setup.md) for the bundled commands and [Resolve operations](references/resolve.md) before touching Resolve. If Resolve is unavailable, complete the catalogue, questions and scene plan; report native editing as pending. A generated XML file is not evidence of an imported or working Resolve timeline.

## Reconstruct the story

Read [story and context](references/story.md). Catalogue all footage, including non-speech clips. Separate observed facts, metadata, author memories and assumptions. Treat file timestamps, photo GPS and travel bookings as clues that can conflict. Use photos or selected emails only within the user's authorized sources; without them, ask focused questions and continue with known context.

View candidate ranges in motion and with surrounding context. A transcript or contact sheet alone cannot establish a good cut. Map place → action → reaction/result → ending. Ask for memories where they change the story; never invent a remembered event or causal connection between different days.

## Edit a bounded scene

Read [editing principles](references/editing.md) and the user's preferences. Describe the intended change and protected material, then duplicate the timeline or create a new named version. Track source ranges, frame rates and why each shot contributes new information. Preserve complete selected thoughts, real reactions and meaningful motion. Adapt pacing to the scene, not a fixed shot length.

Draft voiceover from confirmed memories. Let the author record it; do not fabricate missing family dialogue. Optional music, sound effects and models are choices, not required subscriptions. Record their provenance and check the actual resulting mix.

## Verify, review and learn

Read [checks](references/checks.md) for each new export or sound change. Compare the native timeline and actual rendered file. Identify the reviewed version by hash; distinguish measured, transcribed, model-reviewed, watched/listened and accepted by the author. Report untested intervals and unavailable checks. A command returning success is not artistic approval.

Apply feedback with [review and memory](references/review.md). Keep the original comment, timecode/version, concrete change and verification evidence. Reusable taste belongs in preferences; one-off cuts belong in the scene's feedback. Previous approval of an idea does not accept its execution.

Deliver the editable project plus a clearly labelled review export, remaining limitations and a short project status. Upload to Replay or publish on YouTube only within an explicit publishing instruction; preserve earlier versions and verify the actual delivered file. Save selected delivery metadata locally, not in the reusable skill.

## Bundled resources

- `scripts/project.py`: workspace initialization, read-only catalogue, tool discovery, export measurement.
- `scripts/timeline.py`: validated, video-only straight-cut FCP 7 XML from an explicit shot plan. It is a technical interchange helper, not an automatic story editor or complete audio conform.
- `scripts/resolve_bridge.py`: read-only connection probe and guarded XML import into an already open, empty, explicitly named project.
- `assets/templates/`: blank preferences, scene, feedback and status files. Copy them into the user's project; do not write personal data into the installed skill.

Paths in commands are supplied by the user or discovered locally. Helper scripts use only Python's standard library; FFmpeg/ffprobe and Resolve are separate optional executables. See the references for command arguments and limits.
