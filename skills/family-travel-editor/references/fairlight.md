# Fairlight: preserve the intended mix

Read this when using Resolve's AI Audio Assistant or replacing music after an automated mix. This is an optional native-editor procedure, not a bundled helper or a required step for each export. It draws on a production trial in Resolve Studio 21.1.1 on macOS on 31 October 2026; check the installed version and available tools before acting. That trial does not validate this package's XML importer.

## Before Auto Mix

Save the original project and work in a named timeline copy. Apply [preservation](preservation.md): record sources, source ranges, timeline positions, enabled/mute state, transitions and processing. Include track/bus automation, not just clip gain. Identify dialogue, narration, music and atmosphere; avoid mixing speech and music roles on the same track where classification depends on track type.

Write down the musical intent at important ranges: quiet conversation bed, deliberate pause, music returning to lead, and protected ending. These are scene-specific decisions, not universal loudness targets. Keep a reference export for comparison.

Use the installed version's supported controls. The originating trial used Timeline → AI Tools → Audio Assistant in the UI; it did not establish an API call for this operation. Confirm the active project and copied timeline before starting. If the tool is unavailable, continue with the existing mix or a manual plan; do not claim the assistant ran.

## After Auto Mix

Match clips by source range and timeline time, not track number alone: the assistant can regroup tracks and add transitions. Check the speech edges of new crossfades and confirm every intended sound reaches the master.

Render the changed mix and compare with the reference at matched playback loudness. Then compare relative levels across the intended musical ranges. A louder overall export can still flatten or reverse a deliberate musical lift. Retained clips and a successful command do not establish that the mix is right.

If a contrast or transition changed undesirably, correct that range in the copy and check the actual result. Listen to the affected scene and adjacent context; use [export checks](checks.md) for the full delivery. Keep the original and revised versions separately.

## When replacing music later

Copying a clip's properties, including Resolve `GetProperty` / `SetProperty` values, does not establish preservation of track/bus automation or the audible result. Capture the relevant processing before replacement, retain intended timing and fades, and export the changed scene again. Compare the quiet bed, leading music, speech boundaries and ending. Reuse previous review evidence only for unchanged signal/ranges as described in [checks](checks.md).

Record the editor version, timeline/export identity, intended versus observed differences, corrections and listening coverage. Measurements support this review; they do not prove timbre, musical quality or filmmaker acceptance.
