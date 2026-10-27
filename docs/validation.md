# Validation coverage

## v0.2.0 — 27 October 2026

| Area | Observed result | Limits |
|---|---|---|
| Local tests | 13 passed on macOS, Python 3.9.6, FFmpeg/ffprobe 7.1 | Includes a real video render, clean installation, update backup, workspace, XML, invalid input and overwrite refusal |
| Free preview route | Rendered the included v2 plan: 250 frames, 25 fps, video stream only | Synthetic same-rate H.264 fixture; no sound or native editable project |
| Input mismatch | Incorrect source frame count and frame rate rejected before delivery | No complete variable-frame-rate certification; normalize separate copies when needed |
| Skill structure | Bundled skill validator passed | Does not prove automatic discovery or editorial quality |
| Python and whitespace | Compilation and `git diff --check` passed | Functional coverage is the test suite above |
| Real film illustration | Still extracted from the author's local final master; chapter/revision links use the recorded public YouTube publication | Not a demonstration of this starter package producing the full film; links show final result, not before/after |
| Resolve native round trip | Deferred: another editing session owns the active Resolve project | No claim of tested native import, playback or export |
| Other editors | Official Shotcut, Kdenlive and libopenshot documentation reviewed | No shipped or tested native adapter for those editors, iMovie or CapCut |

CI installs FFmpeg and runs the helper/media suite on Python 3.9 and 3.12. The live workflow run is the authority for CI status; the table above records local validation.

The preview renderer probes/counts inputs, refuses incompatible plans, renders to a temporary file and checks the output frame count. Its output is explicitly silent. Do not use it as an audio-preserving conform tool.

The local validation tools were isolated outside the repository. FFmpeg came from imageio-ffmpeg; ffprobe was compiled locally from official FFmpeg 7.1 source with just the components required by the H.264/MP4 fixture. Tool binaries, source archives and build environments are not included in the package.

## Earlier release record

### v0.1.0 validation

Checked on 26 October 2026. These results describe this release's helpers and synthetic fixture, not an independently reproduced full family-film edit.

| Area | Result | Limits |
|---|---|---|
| Agent Skill structure | Passed bundled skill validator | Structural check, not a behavioural guarantee |
| Portable plugin manifest | Passed official Agent Plugins 1.0.0 JSON schema | OpenAI portal checks not yet run |
| Helper tests | 8 passed with Python 3.9.6 | Range bounds, path containment, overwrite refusal, catalogue identity, protected Resolve-project guards |
| Clean skill copy | Installed into a separate temporary directory | No global client configuration changed; automatic discovery not exercised |
| Workspace creation | Blank templates created from that isolated skill | Existing-workspace refusal retained |
| XML generation | 250-frame v2 timeline generated outside source tree | FCP 7 XML, video only, 25 fps |
| Synthetic media | Full FFmpeg decode succeeded; v1 300 frames, v2 250 frames | No audio, people, geographic context or narration |
| Protected first/last shots | 10 corresponding decoded frames compared; maximum mean absolute RGB difference 0.0 | Sampled image preservation, not a full artistic review |
| Live Resolve connection | Unavailable | Native import, playback and Resolve rendering are NOT validated |
| Optional services and models | Not exercised | Gmail, Photos, Replay, YouTube and audio models are not bundled |
| ChatGPT public directory | Not submitted at build time | Installation, publisher verification, portal checks and approval remain external steps |

The synthetic render initially exposed a frame-duration issue at the final encoded frame. The generator now specifies a constant output rate; the final files were decoded and counted again. The checked-in previews are FFmpeg renders, not Resolve exports.

For native verification: regenerate XML for local media paths, open a fresh empty Resolve project, import, confirm 25 fps and 250 frames, inspect all three shots, render and compare the actual output. Do not run this experiment inside an existing family-film project.

The complete helpers use the Python standard library. Release validation additionally used FFmpeg 7.1 from imageio-ffmpeg 0.6.0, PyYAML 6.0.3 and jsonschema 4.26.0 in an isolated temporary environment. Those dependencies and their environments are not part of the package.
