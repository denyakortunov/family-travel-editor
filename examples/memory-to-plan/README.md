# A first planning session — before footage is available

This is a **recorded independent agent trial on 29 October 2026**, using Family Travel Editor 0.3.1 in a Codex agent session on macOS / Python 3.9.6. The starting memory is the public author answer already described in the repository: a mountain trip for cooler weather than Singapore, with sweaters, tea and a fireplace. The follow-up is an explicitly simulated tester instruction.

**No travel footage was supplied or inspected. No film was assembled.** This demonstrates a useful planning step and saved continuation, not automatic video editing, a user testimonial or a human usability study. Local machine paths in the saved outputs have been replaced with placeholders.

## 1. The request

> Help me plan one travel scene. We went to the mountains because we wanted cooler weather than Singapore. I remember sweaters, tea and a fireplace. I have no footage available in this session, my editor is undecided. Give me a useful provisional plan and a saved next step, without making up shot ranges or claiming to view clips.

The agent read SKILL.md and its first-run, story, editor, setup, editing and review references. It created a separate temporary workspace, ran the planning doctor and installation self-test, then wrote plan-v1. It did not read private film material as evidence.

## 2. What actually ran

| Action | Observed result | Limit |
|---|---|---|
| `project.py init <trial-workspace>` | Exit 0, new workspace created | No editor project |
| `project.py doctor --task plan --json` | Exit 0, version 0.3.1, READY | FFmpeg/ffprobe not found on this session's PATH; no editor probe |
| `self_test.py` | Exit 0, PASS | Fake metadata fixture; no real footage or rendering |
| Plan and revision comparison | Protected fields unchanged; v1 retained | Written-plan checks only |

[Doctor output](doctor-plan.json) · [Self-test output](self-test.txt) · [Artifact checks and hashes](verification.json).

## 3. The useful output

The [readable plan](readable-plan.md) proposes a conditional progression: orient in the mountains, develop the remembered contrast through available sweater/tea material, then find an ending supported by the footage. It leaves source filenames, ranges, duration, chronology, speech and music undecided. A fireplace is a possible ending to check, not an invented shot.

The table gives the filmmaker something concrete to look for when reviewing the clips. Missing footage does not prevent this provisional plan, but it prevents choosing verified shot ranges. [Structured plan](scene.json) · [Preserved v1](versions/v1-scene.json).

## 4. One bounded revision

The tester supplied this **simulated scene-only instruction**, not a new real author preference:

> Keep this scene without added narration; leave original speech decisions open until we can hear the footage.

The agent created plan-v2. Only version, audio and change-basis fields changed in the structured scene. Added narration is now excluded for this scene; original speech remains open. It preserved v1 and left reusable preferences empty. [Feedback and verification scope](feedback.json).

This is verified in the written plan, not accepted by an author or applied to an actual timeline.

## 5. Continue it yourself

Copy this example directory into a separate working folder. In a fresh chat, ask the agent:

> Read the installed family-travel-editor SKILL.md and then STATUS.md, scene.json, preferences.json and feedback.json in [absolute path to the copied example]. Explain where the plan stands and continue from plan-v2. Preserve the scene-only no-added-narration decision. Do not select shot ranges or original speech until actual footage can be inspected and heard.

[STATUS.md](STATUS.md) records the next step: check a supplied source folder, catalogue it outside the originals, inspect candidate clips in motion, build genuine visual coverage, then listen before selecting speech. Once source ranges are real, use a [manual assembly plan](../../docs/manual-assembly.md) or a separately verified editor integration.

A different agent may word the plan differently. The useful expectations are grounded evidence, explicit gaps, preserved revisions and an actionable next step—not identical prose or a promised finished film.
