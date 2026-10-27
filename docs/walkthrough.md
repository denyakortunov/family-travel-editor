# Walkthrough: make one edit, check what changed

A small, reproducible use case for an AI editing agent. Start with three clips, make a 12-second preview, then shorten the middle shot to produce a 10-second revision.

**These are generated test patterns, not travel footage.** They let you inspect timing and preservation without personal media, paid services or an editor account. The example demonstrates the mechanics of a revision; it does not demonstrate automatic storytelling, listening or a finished film.

[Play V1 — 12 seconds](../examples/first-scene/generated/v1.mp4) · [Play V2 — 10 seconds](../examples/first-scene/generated/v2.mp4) · [Browser walkthrough](walkthrough.html)

The HTML walkthrough includes side-by-side video players. To use it, download the repository and open `docs/walkthrough.html` in a browser; GitHub's file view shows HTML source rather than running the page. Everything also works as this illustrated GitHub document.

## 1. Start with material you can inspect

All three source files are 640 × 360, 25 fps and four seconds long. Each contains 100 frames and no audio. These images are actual frames extracted from the included clips.

| Shot 1 · opening | Shot 2 · middle | Shot 3 · ending |
|---|---|---|
| ![Actual frame from synthetic shot 1](walkthrough/shot-1.jpg) | ![Actual frame from synthetic shot 2](walkthrough/shot-2.jpg) | ![Actual frame from synthetic shot 3](walkthrough/shot-3.jpg) |
| [Source clip](../examples/first-scene/generated/media/shot-1.mp4) | [Source clip](../examples/first-scene/generated/media/shot-2.mp4) | [Source clip](../examples/first-scene/generated/media/shot-3.mp4) |

For your own footage, this is where the agent inventories files and checks what it can actually view and hear. Metadata establishes duration and frame rate; it does not establish what happened in the scene.

## 2. Give the agent a bounded task

This is a suggested prompt you can run, not a transcript of an autonomous agent session:

> Read `skills/family-travel-editor/SKILL.md` and `examples/story-to-cut/README.md`. Use the included synthetic clips. Explain the three-shot plan, then render V1 into a new temporary folder. Keep all source files unchanged. Use FFmpeg; no Resolve or service account is needed. Report the output duration, frame count and whether it has audio.

The human supplies the goal and constraints. The agent reads instructions and chooses available tools. The scripts perform the specified operations. The included narrative example assigns opening → action → result roles; test patterns cannot prove those storytelling roles visually.

On a real trip, ask a question only when its answer changes the edit: “What happened before this moment?” Store the author's answer separately from visible evidence. Photos or selected travel records can provide context when available, but are not required for this test.

## 3. Turn the plan into the first cut

The [V1 plan](../examples/first-scene/generated/v1.json) selects all 100 frames of each clip, in order. At 25 fps, 100 frames means four seconds.

| Order | Source range | Timeline range | Purpose in this example |
|---|---|---|---|
| 1 | shot-1 · frames 0–99 | 0–4 seconds | Opening to preserve |
| 2 | shot-2 · frames 0–99 | 4–8 seconds | Middle shot to revise |
| 3 | shot-3 · frames 0–99 | 8–12 seconds | Ending to preserve |

The JSON uses an exclusive `out`: `in: 0, out: 100` selects frames 0 through 99. The renderer follows these ranges; it does not decide which moments are interesting.

**Output:** [V1 video](../examples/first-scene/generated/v1.mp4), 12 seconds, 300 frames, silent.

## 4. Give one precise correction

> V1, 00:00:04:00: shorten the middle shot by two seconds. Preserve the first and last shots.

The timecode refers to V1 at 25 fps. Only `shot-2` changes: its exclusive `out` becomes 50 instead of 100. The opening retains frames 0–99; the ending retains frames 0–99 and starts two seconds earlier on the timeline.

![V1 and V2 timelines at the same scale: only the middle shot gets shorter](walkthrough/timeline.svg)

**Output:** [V2 video](../examples/first-scene/generated/v2.mp4), 10 seconds, 250 frames, silent. Compare [V1 plan](../examples/first-scene/generated/v1.json) and [V2 plan](../examples/first-scene/generated/v2.json).

## 5. Check the result and keep the decision

| Check | Expected evidence | What it does not establish |
|---|---|---|
| Correct duration | V1: 300 frames; V2: 250 frames; both 25 fps | Whether the pacing feels good |
| Bounded change | Only the middle shot's out-point changes in the plans | Whether a larger project kept its sound and effects |
| Source preservation | First and last source ranges match between versions | Approval by the person making the film |
| Actual output | Decode and inspect the MP4s, including both cuts | Audio quality: this fixture has no audio |

The [feedback record](../examples/story-to-cut/feedback.json) links the request to V1 and the change to V2. Its status is **applied**, with an explicit verification method; no author acceptance is claimed. The [preferences file](../examples/story-to-cut/preferences.json) stays empty: shortening this shot is not a rule that every shot should be two seconds long.

For a real project, check the full affected context, including sound, titles and later scenes. An agent's completion message is not a substitute for inspecting the exported file.

## 6. Reproduce it, then try your own scene

You need Python 3.9+, FFmpeg and ffprobe. From the repository root:

```sh
python3 skills/family-travel-editor/scripts/project.py doctor --task preview
python3 examples/first-scene/make_demo.py --output /path/to/new-demo
```

Use a new directory. The generator produces source clips, V1/V2 plans, previews, feedback and XML files with local media paths. It refuses to overwrite an existing directory.

To render a supplied plan through the preview helper:

```sh
python3 skills/family-travel-editor/scripts/render_preview.py examples/first-scene/generated/v2.json --media-root examples/first-scene/generated/media --output /path/to/new-v2.mp4
```

[Full commands and editor import limits](../examples/first-scene/README.md) · [Recorded validation](validation.md)

### What carries over to a real travel scene?

| Step | You provide | The agent helps with | Your decision |
|---|---|---|---|
| Understand the material | Clips and any relevant memories | Catalogue, inspection, questions, transcript when available | Which moments matter |
| Plan a scene | Intended story and audience | Scene outline, shot ranges, draft narration | Confirm the facts and tone |
| Assemble | Preferred editor and available tools | Preview or supported timeline preparation | Review the first cut |
| Revise | Version + timecode + request | Scoped change and comparison | Accept it or request another revision |
| Finish | Recorded voice, music and publication choices | Checks and delivery preparation through available tools | Listen, watch and approve release |

The skill does not bundle an autonomous full-film editor. The included renderer produces silent straight cuts. Audio mixing, titles, native editor operation and publication need appropriate tools and separate verification. iMovie and CapCut can use the plan and feedback workflow with manual assembly; no native adapter for them is included.

[Start your own scene](../README.md#start-with-one-scene) · [Choose your editor](../skills/family-travel-editor/references/editors.md)
