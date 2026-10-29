# What’s New in v0.3.2

29 October 2026 — a real-footage example you can run and resume.

## Added

- A Grand Canyon picture-edit exercise using public-domain NPS footage: three prepared clips, a narrative plan, exact source ranges, two previews and a bounded revision from 24 to 22 seconds.
- One command runs the example without downloads. It checks source identities, builds the catalogue, renders both silent previews and prepares video-only XML.
- A generated workspace STATUS plus copied plans, feedback and preferences let a fresh chat continue from the actual result.
- Original source URLs, credits, hashes and transformation details. An optional preparation script downloads verified NPS originals and regenerates separate copies.
- A documented independent Claude trial that actually ran the exercise and inspected its outputs, alongside local automated checks. This is an agent evaluation, not a study with new human users.

## Fixed after the trial

- Installation self-test no longer emits a misleading “install ffprobe” warning from its deliberately metadata-only fixture.
- XML generation no longer sends every user to Resolve; it states that native import, playback and export still require verification.
- Temporary preview encodes now use the system temporary directory instead of the result directory. Hidden staging copies had been observed remaining in a cloud-synchronized result folder; their exact reappearance mechanism was not established.
- Measurement commands print the result path and scope.
- The example refuses output inside its supplied source directory and refuses to replace an existing workspace. Its preparation resets timestamps and uses explicit frame counts to handle the original 24000/1001 fps footage correctly.

## Try it

From the extracted source ZIP, with Python 3.9+, FFmpeg and ffprobe:

```sh
python3 examples/grand-canyon-sunset/run_demo.py --output "sunset-demo"
```

Open v1.mp4 and v2.mp4 in that folder. To continue in a fresh chat, point your agent to the installed SKILL.md and the generated sunset-demo/STATUS.md.

## Updating

Download the source ZIP and run `tools/install_skill.py --destination YOUR_EXISTING_SKILL_DIRECTORY --update` with your Python interpreter. Use the same destination as before; the old copy is preserved in a sibling backup directory. Film workspaces are not overwritten. Run the printed self-test command, then open a new chat. The example belongs to the source ZIP; it is not a runtime dependency of the smaller installed skill/plugin package.

## Limits

The real-footage exercise is intentionally silent. Original source audio is excluded; this is not dialogue/music editing or a complete family film. The prepared copies are 640×360 at 25 fps, normalized from NPS sources. Frame inspection and measurements do not establish uninterrupted watching, listening or artistic approval. Native editor integrations remain separately unvalidated. No personal footage is included and no NPS endorsement is implied.

[Download v0.3.2](https://github.com/denyakortunov/family-travel-editor/releases/tag/v0.3.2) · [Real-footage example](https://github.com/denyakortunov/family-travel-editor/tree/v0.3.2/examples/grand-canyon-sunset) · [Validation](https://github.com/denyakortunov/family-travel-editor/blob/v0.3.2/docs/validation.md)
