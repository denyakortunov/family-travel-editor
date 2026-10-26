# v0.1.0 validation

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
