# CapCut Web through an optional plugin

Use this route when the user wants a browser-based, editable timeline and their agent has the official CapCut plugin. The tested connection was CapCut's Codex plugin 0.2.7. Installing Family Travel Editor does not install or connect CapCut. The desktop app is not required for this Web route; desktop automation and the same connection in other agent hosts were not tested.

## Start with one small scene

1. Install the CapCut plugin offered by your agent host and connect your CapCut account through its authorization flow. Use the plugin's current setup instructions; do not copy credentials or configure an undocumented endpoint.
2. Verify that the account-bound editing tools are available. A connected account alone does not prove that this chat can call them. Preserve progress if the host needs a continuation to load newly installed tools; do not repeat an upload or submitted edit.
3. Use a few non-sensitive clips first. This route uploads media to CapCut; it is not a local-only edit. Keep the originals and use a separate test project.
4. Ask the agent to assemble a short scene, inspect the returned editable clips, make one bounded revision, save it and read the project back. Review the result in the returned CapCut Web editor.
5. Use the Web editor's export workflow for the final file when no export tool is exposed. Check the actual exported file's duration, picture and sound. A saved cloud project is not an exported movie.

Example first request:

> Use Family Travel Editor with my connected CapCut plugin. Assemble these three clips in order with straight cuts and their original audio. Return an editable project. Then shorten the middle clip by one second and move the last clip to close the gap. Read back the saved project and explain how to export it. Do not add generated media, templates or music.

The skill is free; CapCut account features and usage limits are separate. This trial does not establish which operations are free for every account or region. Check the account's actual entitlement before a paid operation.

## Continue an existing edit

Use the installed plugin's editing, draft-builder and collaborative-editing instructions for exact tool contracts. Reuse the existing upload, AI task and draft session rather than creating duplicates. An AI rough-cut session is different from a cloud-draft session.

Inspect a rough cut before importing it: a returned draft may contain separate source clips or only a flattened render. Only the former exposes the original cuts for editing. Importing a rough cut into a new collaborative session creates a separate editable copy; tell the user which project is being revised.

Before changing a cloud draft, check its version and preserve newer browser edits. Apply the supported atomic operations, save once and inspect the server-returned draft. For a tail trim, shorten the middle clip and move the next clip to its new start; changing timeline placement alone does not change the source in-point. Do not present an earlier rough-cut preview as the export of a later revision.

## Verified on 4 November 2026

Three synthetic 1280×720 clips, each four seconds at 25 fps with stereo 48 kHz audio, were uploaded through the official plugin. AI Lab returned a 12-second movie and a draft containing three separate source clips. A collaborative cloud copy was saved and read back. The middle clip was then shortened to source range 0–3 seconds and the third moved to second 7. A second save/read-back confirmed an 11-second project with the original source bindings and three editable clips.

Independent inspection of the first rendered file found 360 video frames at **30 fps**, rather than the requested 25 fps, and stereo **44.1 kHz** audio rather than the source's 48 kHz. These conversions matter when matching an existing film's technical settings. Do not promise exact source frame-rate or audio-rate preservation from this rough-cut path.

No post-edit export endpoint was exposed in the tested plugin. The revised 11-second movie export, independent browser reopen, playback/audio quality, long-form travel editing and free-plan availability remain unverified. Basic cloud assembly and saved revision are the supported, tested scope; a complete unattended delivery workflow is not certified.

[CapCut](https://www.capcut.com/) supplies the editor and account service. Consult the installed plugin's own versioned instructions for current commands.
