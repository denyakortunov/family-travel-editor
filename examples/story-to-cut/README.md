# A filled story, feedback and memory example

This is a **synthetic teaching example**, not a transcript of the author's family trip. The three test-pattern clips stand in for setup → action → result. The real film is linked separately in the [case study](../../docs/real-film.md).

1. Read [scene.json](scene.json): facts, a question, scene structure and intended shot roles. There are no fabricated memories or dialogue.
2. Resolve those roles to the included fixture's measured source frames. The [v1 shot plan](../first-scene/generated/v1.json) has three four-second shots. This is the technical JSON accepted by `timeline.py` and `render_preview.py`; the narrative `scene.json` is not.
3. Read [feedback.json](feedback.json): the request belongs to v1, protects the opening/ending and produces v2. The [v2 plan](../first-scene/generated/v2.json) changes only the middle shot from 100 to 50 frames.
4. Compare the [previews](../first-scene/README.md). A successful render establishes timing, not storytelling quality or author acceptance.
5. Read [preferences.json](preferences.json). The example deliberately has **no new global preference**: “shorten this shot” is a one-off instruction. A reusable preference needs a separate explicit statement and its provenance.

A useful question for a real arrival scene would be: “What did you think would happen here, and what actually happened?” Record the answer as a memory, not as a fact observed in the image. If the answer is missing, leave the question open and keep the scene factual.

## Resume prompt

> Read this film workspace's STATUS.md, scene.json, preferences.json and feedback.json. Continue from v2. Preserve the first and last source ranges. The example feedback is applied but not accepted. Report what can be checked from the files and what still requires watching/listening or the author's decision.

## From a correction to a reusable preference

Only if the author separately says “Across my films, keep the reaction after a joke,” add a preference with the exact quote, date, originating feedback ID and scope. Do not turn a request to shorten one shot into a universal maximum shot length. A stored preference guides future decisions; it does not train model weights or prove another computer has the updated project.
