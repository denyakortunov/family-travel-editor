# From a plan to your editor

A readable scene plan is useful even when your agent cannot control the editor. Ask it for a table with source, IN/OUT and units, shot role, speech, music and transition. For real footage, ranges require inspection; leave them unselected until that happens. The narrative `scene.json` is different from the technical JSON accepted by the preview/XML helpers.

## Repeatable exercise: three synthetic shots

This exercise uses the supplied [color-bar clips](../examples/first-scene/generated/media). They contain no travel, people, dialogue or music. The story roles below are teaching labels, not observations about real events. You can copy the exercise into a new project in iMovie, CapCut or another editor; this is a manual procedure, not a tested native adapter.

| Order | Source | Source range (OUT exclusive) | Length | Role | Speech / music | Transition |
|---|---|---|---|---|---|---|
| 1 | `shot-1.mp4` | 0–100 frames at 25 fps, 0–4 s | 4 s | Setup stand-in | None in fixture | Straight cut |
| 2 | `shot-2.mp4` | v1: 0–100; v2: 0–50 frames, 0–2 s | v2: 2 s | Action stand-in | None in fixture | Straight cut |
| 3 | `shot-3.mp4` | 0–100 frames at 25 fps, 0–4 s | 4 s | Result stand-in | None in fixture | End |

1. Create a new project and import the three clips without changing the originals. Use 25 fps if the editor exposes that setting. If it does not, distinguish the intended source ranges from the editor's output rate.
2. Place the clips in this order at four seconds each. Save v1: 12 seconds.
3. Duplicate the project/timeline as v2. Trim only the end of the middle shot to two seconds and close the gap. Preserve the opening and final shot's source ranges.
4. Play the sequence and check all three shots and both joins. Export a separately named review copy. The intended v2 duration is 10 seconds; the bundled 25 fps helper export is 250 frames.
5. Record the actual editor, settings, source ranges and export checks in STATUS. Do not claim frame-accurate preservation in an editor that has not been verified.

The [feedback record](../examples/story-to-cut/feedback.json) shows the versioned request. It remains applied, not author-accepted. [Resume from the saved example status](../examples/story-to-cut/STATUS.md).

## Translate this into a real scene

Use real source filenames and verified ranges. Replace stand-in roles with what each shot contributes. Preserve complete selected speech and reactions; do not trim them mechanically to this exercise's duration. Specify whether original ambience continues across each cut, where music leads and where it becomes quiet under speech. Do not add music merely because a table has a column for it.

If listening or viewing is unavailable, mark those decisions open. The next useful action is to inspect a candidate range or ask a specific memory question, not invent precise timings. The [memory-to-plan session](../examples/memory-to-plan/README.md) demonstrates this earlier stage.
