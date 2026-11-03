# Validation coverage

## v0.3.11 — 4 November 2026

CapCut Web through the official Codex plugin 0.2.7: three synthetic uploads, a 12-second AI rough cut with three separate editable clips, cloud import/save/read-back, middle-clip tail trim to three seconds and a second cloud save/read-back completed. Independent comparison confirmed source order and bindings, 1280×720 canvas, one video track and contiguous 4/3/4-second clips ending at 11 seconds.

The first rendered MP4 contained 360 frames at 30 fps and stereo 44.1 kHz audio; inputs were 25 fps/48 kHz. Container duration was approximately 12.005 seconds. The revised 11-second project was not exported: no separate post-edit export endpoint was exposed in this plugin. Browser reopening, playback/listening, desktop control and account-wide free/paid entitlement were not certified. See [CapCut setup and limits](../skills/family-travel-editor/references/capcut.md). No helper behavior changed.

## v0.3.10 — 4 November 2026

Final Cut Pro Creator Studio 12.4 / Apple Silicon, third-party FCP MCP Server 0.30.0: stdio MCP initialization, library inspection, generated three-clip FCPXML, native import, middle-clip trim, connected-audio addition and revised import completed. Read-only native queries confirmed 12-second and 11-second sequences at 25 fps. Test libraries were separate from existing films.

The external FFmpeg preview used 24 fps and the revised XML retained a stale 12-second sequence duration; Final Cut reported the actual 11-second clip extent. No native movie export, save/reopen cycle, uninterrupted playback or listening was certified. See [the exact workflow and limits](../skills/family-travel-editor/references/final-cut.md). No CapCut native editing claim is added.

## v0.3.9 — 2 November 2026

| Area | Observed result | Limits |
|---|---|---|
| Local helper/media suite | 28 tests passed on macOS / Python 3.9.6 with FFmpeg/ffprobe available, including silent rendering, bounded revision, installation and release guards | No new helper behavior; synthetic and public picture fixtures do not validate sound or native editors |
| Source and plugin packages | Both archives extracted outside the repository; checksums and file contents verified; self-test passed and planning doctor reported READY; both new references present | Filesystem/package validation, not marketplace approval or in-app discovery |
| Update from v0.3.8 | Installed the previous version, added a test note, then updated from the extracted v0.3.9 source package using a relative destination containing spaces | Temporary destination; no personal agent configuration changed |
| Update preservation | Previous version and test note preserved in the sibling backup; existing film workspace hashes unchanged; updated self-test passed | Does not certify every filesystem or operating system |
| Structure and documentation | Skill validator, Python compilation, whitespace and local Markdown file-link checks passed; new release notes use absolute versioned documentation URLs | Live release URLs become available only after publication |
| New sound instructions | Compared with the originating project's Fairlight trial and sound-sync procedure; Epidemic Sound guide checked against official MCP documentation on 2 November | No new Fairlight session, paid library operation, listening trial or native adapter certification performed for this release |

The [release workflow](https://github.com/denyakortunov/family-travel-editor/actions/workflows/check.yml) runs the suite on Ubuntu 24.04/Python 3.9 and 3.12 and publishes only after both pass. Its run for the tagged commit is authoritative for remote validation. An initial attempt stopped during Python setup on the new Ubuntu 26.04 default, before any test ran. Pinning Ubuntu 24.04 retains the 3.9 check; the official [Python build manifest](https://github.com/actions/python-versions/blob/main/versions-manifest.json) lists compatible builds. The Shotcut draft remains excluded; no complete sound edit or autonomous film is claimed.

## v0.3.2 — 29 October 2026

| Area | Observed result | Limits |
|---|---|---|
| Real-footage exercise | Three normalized NPS source copies rendered into 600-frame v1 and 550-frame v2 at 25 fps | Silent picture edit; no native editor or original-audio evaluation |
| Protected material | All frames compared at 160×90: protected first 400 frames mean absolute RGB difference 0.0054/255; retained final 150 frames 0.4529/255 | Compression differences; no claim of pixel-identical encoded outputs or artistic approval |
| Independent Claude trial | Claude Opus 5.5 ran doctor/self-test/example, inspected hashes, XML and frame counts, performed frame comparisons and inspected 14 still frames | No uninterrupted playback, listening, real human-user study or acceptance |
| Trial findings | Resume state added; misleading self-test/editor messages corrected; staging moved outside result directory | Cloud-sync residue observed, underlying synchronization mechanism not established |

[Actual public example and source rights](../examples/grand-canyon-sunset/README.md) · [Agent test scope and outcomes](agent-trials.md). The final local suite has 28 passing tests, including real rendering and continuation files. The release CI run is authoritative for the final Python 3.9/3.12 suite.

## v0.3.1 — 29 October 2026

| Area | Observed result | Limits |
|---|---|---|
| Local helper/media suite | 24 tests passed on macOS / Python 3.9.6; includes real silent preview rendering, catalogue timeout/error recovery and unreadable-directory detection, missing source and relative install paths | Timeout/read failures are injected; candidate extensions are not codec certification |
| Independent first use | A separate Codex agent read the skill, initialized a temporary workspace, passed doctor/self-test and saved a provisional plan plus a bounded revision | No footage, editor, human user or artistic acceptance; [actual session](../examples/memory-to-plan/README.md) |
| Version-to-version update | Installed v0.3.0, added a local note, updated from the v0.3.1 source ZIP using a relative path with spaces; old version and note preserved in backup, printed self-test command passed | Temporary destination, no personal agent configuration changed |
| Structure and packaging | Skill structure and Python compilation checked; clean source/plugin extraction and self-tests exercised by suite | No marketplace certification |

The exact release CI run remains the authority for Linux/Python 3.9 and 3.12. Installation does not establish app discovery or video/audio understanding. See [capabilities](capabilities.md).

## v0.3.0 — 29 October 2026

| Area | Observed result | Limits |
|---|---|---|
| Local helper/media suite | 17 tests passed on macOS / Python 3.9.6, including a real silent render and mocked publication failure/idempotence checks | Synthetic footage; no artistic or speech-quality claim |
| Source and plugin archives | Built, checksum-verified, extracted and self-tested in temporary folders | Plugin archive structure tested; no marketplace/client import certification |
| Clean Python installation | Installed from extracted source ZIP; self-test passed from outside the skill folder | Does not prove UI discovery in every client |
| Third-party skills CLI | skills 1.7.4 installed the local release folder for Codex, Claude Code and Cursor; installed self-test passed | Filesystem installation, not in-app invocation; remote tagged install checked after publication |
| Editorial procedures | Compared with current editing rules; family-specific paths, identities, film queues and licensed media excluded | Instructions, not a bundled motion model or full-film automation |
| Native editors and acoustic review | No new certification | Resolve round trip remains unvalidated; draft Shotcut adapter excluded; human listening still needed |

The current CI run is authoritative for its Python 3.9/3.12 results and publication. Source packages include tests; installed skills are self-contained without the repository's tools or examples. Installation self-test uses fake metadata, not playable footage. The optional existing media fixture remains clearly labelled as color bars.

## v0.2.0 — 27 October 2026

| Area | Observed result | Limits |
|---|---|---|
| Local tests | 13 passed on macOS, Python 3.9.6, FFmpeg/ffprobe 7.1 | Includes a real video render, clean installation, update backup, workspace, XML, invalid input and overwrite refusal |
| Free preview route | Rendered the included v2 plan: 250 frames, 25 fps, video stream only | Synthetic same-rate H.264 fixture; no sound or native editable project |
| Input mismatch | Incorrect source frame count and frame rate rejected before delivery | No complete variable-frame-rate certification; normalize separate copies when needed |
| Skill structure | Bundled skill validator passed | Does not prove automatic discovery or editorial quality |
| Python and whitespace | Compilation and `git diff --check` passed | Functional coverage is the test suite above |
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
