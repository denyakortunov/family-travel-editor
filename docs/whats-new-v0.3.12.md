# What's New in v0.3.12

4 November 2026

- A first invocation now starts a guided conversation about the trip and footage, the desired film and any editor the user already uses. No finished scene idea is required; free-form and partial answers are welcome.
- The agent uses known answers, asks a few relevant questions at a time, and suggests the next step. Narration, music and memories are discussed when actual scenes make them useful.
- New workspaces include `BRIEF.md` for trip-specific answers, proposals and open questions. Existing work resumes from its saved state; adding a missing brief does not reinitialize the project.
- Updated the installer and skill/plugin launch prompts. Installing alone does not open a chat or start an edit; invoking the skill starts the interview.
- Editor choice follows the user's tools and local/cloud preference. CapCut Web can be proposed when its plugin is available, with upload and export limits explained; it is not a mandatory dependency.

Update the skill to get the new first-run instructions. Existing film workspaces and answers are preserved. This release does not add editor automation or promise unattended CapCut export.

Try: **“Use $family-travel-editor. Help me get started: ask about my trip and footage, build a short brief and guide me to the next step.”**
