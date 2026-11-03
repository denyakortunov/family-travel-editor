# First run: make the next step visible

Use this for installation, “what now?”, or a new filmmaker. Resume an existing film from its status instead of running setup again.

## Establish what is installed

Read VERSION next to SKILL.md. Run `python3 scripts/project.py doctor --task plan` and `python3 scripts/self_test.py` from the skill directory (or use absolute script paths). Both work without an editor, footage or FFmpeg. Do not assume the repository root, tools/ or examples/ were installed with the skill.

Explain in the user's language: this is guidance and local helpers for an agent, not an application that starts editing when installed. State the version, actual ability to view/listen, and supported operations. READY means helper prerequisites are available; it does not mean an editor is connected or a film has been reviewed.

## Open with a short brief interview

Do this on a bare invocation too; the user does not need to know a special setup command. Respond in their language. Check the current conversation and any existing workspace first. Use known answers, skip irrelevant questions and accept a free-form story, a partial answer or “suggest something.” A technical setup check should support the conversation, not replace it. If Python or local helpers are unavailable, explain the specific limitation and still collect the brief in chat.

A new user should see a short welcome and a small first set of questions, for example:

> I’ll help turn your travel clips into a film: find the story, plan the edit and work in your editor. Tell me a little about the trip; you don’t need a finished plan yet.
>
> 1. Which trip is this, and where are the videos? A folder, attached clips or “not ready yet” is enough.
> 2. What would you like to watch or share: a short highlights video, a longer travel film, or should I suggest a format after looking at the footage?
> 3. Do you already use an editor? If not, tell me and I’ll check the available options.

Adapt these questions rather than repeating them verbatim. Usually ask no more than three at once. Do not ask for a folder or editor the user already supplied. Do not assume a family audience or require children in the story. Avoid making a newcomer pick exact IN/OUT points, frame rates, plugins or a first scene before seeing their material.

Then fill only the gaps that affect the next action: intended viewers/destination, approximate length or orientation, film/voiceover language, moments to include or avoid, and whether they want their own narration. Defer detailed music and memories until there are concrete scenes to discuss. Accept “you choose” for creative decisions; label your suggestions as provisional, not user-confirmed facts. Unknown dates, preferences and story details remain unknown. Photos/GPS and selected travel records are optional later clues, not mandatory account connections at signup.

## Choose a workable editor

Keep the user's existing editor when it supports the intended task. Check actual tool availability before promising assembly. If they are undecided, propose one route with a short reason, not an unexplained catalogue of editors. CapCut Web is a useful first proposal for a browser-based start when the official plugin is available in their agent host; read [its tested limits](capcut.md). Explain that footage must be uploaded and that the tested post-edit export still uses the Web editor. Ask about cloud upload before sending media if it has not already been authorized. Choosing an editor does not by itself authorize uploading all footage, spending money or publishing.

For local-only work or a preferred installed editor, inspect available integrations using [editor choices](editors.md). A Codex connection does not prove the same plugin works in Claude or another host. Do not silently pick Resolve Studio or require a paid editor to complete the brief. Without a working adapter, explain the remaining manual assembly step and continue useful planning.

## Save the brief and take the next step

Summarize the intended film in a short connected paragraph: trip, purpose, desired format and the next action. Ask a follow-up only if an unresolved point blocks that action; there is no mandatory approval of every questionnaire answer. When editing was already requested and the required information is available, proceed within that scope.

Save answers in `BRIEF.md` in the film workspace, using the bundled [brief template](../assets/templates/BRIEF.md). `project.py init WORKSPACE` includes it for new projects. For an existing workspace that predates this template, create only the missing brief file after reading its current STATUS, preferences and scene; never reinitialize it or overwrite an existing brief. Separate the user's statements, agent proposals, unconfirmed information and actual access/authorization. Save stable accepted taste in `preferences.json` and the next action in `STATUS.md`; keep trip-specific wishes in the brief. Do not record credentials. On return, resume from these files and ask only what is still missing.

Propose a separate work folder beside the originals when one is not supplied; do not turn filesystem choices into an unnecessary questionnaire. Respect any stated destination, and avoid initializing over existing work. If no writable workspace is available yet, present the brief in chat, say it is not saved, and ask for a usable destination when saving becomes necessary. Never store the user's brief in the installed skill.

If footage is not ready, provide the provisional brief, explain how to supply a folder or a few representative clips, and state the next action. Offer a clearly labelled example only if useful. Do not claim to have reviewed footage or assembled a film. If the user supplies a whole trip but no scene, catalogue the trip and suggest a representative first scene; do not make them solve the story before you start.

If footage is supplied, run `project.py doctor --task catalog --source SOURCE` to check folder access. Explain separately whether you can read files, run helpers, inspect moving images, listen/transcribe, and operate the chosen editor. Mark each capability as tested, unavailable or not yet checked; installed files alone do not establish any of them.

For footage, create a separate workspace using `project.py init` only if it is new. Catalogue the selected media folder outside the originals. For a large trip, inventory the trip and choose one scene for detailed review; report what has actually been watched. Read the catalogue summary and failed/skipped entries. Exit code 2 means empty or partial results need attention; do not hide failed files or infer coverage from the included count. Build visual coverage before speech selection, then a scene plan with facts, source ranges, gaps and useful memory questions. Do not claim a finished scene from metadata alone.

## End the first step with something usable

Link only the files actually produced: the brief and STATUS first, plus a catalogue or scene plan when available. Explain what is ready and the next action. For a footage review, the following structure may help (fill it with observed facts):

- “Installed version …; planning check …; viewing/listening available through ….”
- “I catalogued … files. I inspected … ranges; … remains unviewed.”
- “Here is the proposed scene, the evidence behind it and the questions that affect it.”
- “Next I can assemble … in …; this route preserves … and cannot yet ….”

When the user requested only a plan, stop at that result. When editing is already authorized, continue the scoped work without demanding the same approval again. If no native adapter is available, make the manual assembly plan concrete or use the silent preview when it serves the request; do not pass it off as a dialogue/music edit.

Record accepted preferences and open feedback in the film workspace. Installing or updating this skill must not create film memory inside its own folder.

## Manual assembly and the next session

Alongside the narrative plan, provide a table with source file, IN/OUT and units, shot role, selected speech, music intention and transition. Unknown source ranges stay unknown until inspected. If no editor adapter is available, describe the concrete trim, order and audio actions the user can perform; distinguish a proposed instruction from an action already executed. Read the plan-formats reference before producing a helper shot plan.

Save STATUS with timestamp/timezone, operator role, current version, sources and export identity (or “none”), actual checks, open questions, running processes and the next action. Give a resume prompt pointing to that workspace's STATUS, scene, preferences and selected feedback. Preserve the previous entry; do not manufacture acceptance, viewing or listening evidence.

The helpers run locally, but model and connected-tool operations depend on the user's agent setup. Explain this when choosing a source-processing route; photos and email remain optional.
