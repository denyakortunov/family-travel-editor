# Roadmap

The aim is a repeatable first scene, then an editable film. Items below are plans, not shipped capabilities.

1. Observe first use with 3–5 new users: understanding, installation, useful plan and next-day resume. Record blockers and actual results; agent trials do not replace this.
2. Validate the existing XML adapter in a clean native Resolve project: import, playback, export and source relinking, with version/platform evidence.
3. Complete the experimental [Shotcut/MLT adapter (draft PR #1)](https://github.com/denyakortunov/family-travel-editor/pull/1): verify opening in Shotcut, source bin and timeline, a trim, Save As, reopening and rendering. Generator/MLT tests do not establish the desktop round trip. The draft is not shipped and mutes source audio. Keep editor-specific metadata out of the shared story plan.
4. Extend the plan and tests for audio, mixed frame rates and transitions before claiming full scene assembly.
5. Add an independently reproduced real-footage walkthrough, with redistribution rights and clear human/agent responsibilities.

Useful contributions: a native round-trip report; a small failing fixture; a tested adapter; clearer first-run instructions. Open an issue describing the result you can demonstrate before building a large integration.
