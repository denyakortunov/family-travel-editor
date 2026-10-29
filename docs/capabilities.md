# Capabilities and limits

Family Travel Editor is an **AI agent skill**, not a standalone editor or an AI model. The skill gives your agent instructions, examples and small local programs. What the agent can see, hear or operate depends on its tools and permissions.

| Task | In this release | What to verify in your session |
|---|---|---|
| Read instructions and plan from your description | Instructions and planning templates | Agent can read the chosen skill/workspace files |
| List footage, hash it and read metadata | Local Python catalogue; ffprobe adds metadata | Source folder readable; check included, skipped, failed and unavailable counts |
| Understand moving images | No video-understanding model bundled | Which viewing tool works, what ranges it actually inspected |
| Listen or transcribe speech | No speech/audio model bundled | Available tool, language coverage and actual reviewed intervals; transcript is not listening |
| Produce a scene plan and revision record | Narrative template and review procedure | Facts, memories, assumptions and unviewed footage remain distinct |
| Render the supplied technical shot plan | FFmpeg silent video preview | ffmpeg/ffprobe available; supported plan/source constraints pass |
| Prepare Resolve interchange | Video-only FCP 7 XML and guarded bridge | Native import, playback and export remain unvalidated |
| Use iMovie, CapCut, Shotcut or Kdenlive | Readable manual assembly plan | No native adapter shipped or certified for these editors |
| Mix dialogue, music, titles and graphics | Workflow instructions | Actual editor/tools and listening/viewing checks required |
| Publish or read photos/email | Optional workflow choices | Separate tools/access and user authorization; no accounts bundled |

The [real-footage exercise](../examples/grand-canyon-sunset/README.md) now demonstrates the silent picture route end to end, including a revision and saved continuation. It does not expand the native-editor or audio capabilities above.

## Installation is a separate check

| Environment | Evidence | Not established |
|---|---|---|
| macOS, Python 3.9.6 | Local helper tests, temporary installation/update, self-test and silent fixture rendering | Automatic discovery in every app; artistic quality |
| Linux, Python 3.9 / 3.12 | GitHub Actions runs the helper and media suite; see the exact release run | Desktop-agent UI or a native editor |
| Codex, Claude Code, Cursor destinations | v0.3.0 installed with skills CLI 1.7.4 and passed the installed helper self-test | In-app invocation, video understanding or native editing in all three products |
| Direct skill reading in Codex | v0.3.1 agent planning trial with no footage; see the recorded session | General user usability, moving-image review or a finished film |
| Windows | Commands documented, no end-to-end Windows test | Installation, shell invocation and rendering reliability on Windows |

The [validation record](validation.md) describes tests by version. The [planning trial](../examples/memory-to-plan/README.md) states its exact scope. Versioned client capabilities can change; check the actual tools in your session rather than assuming that a successful installation supplies them.

## Catalogue results

`catalog.json` keeps the original `files` list and adds `summary`, `skipped` and `scan_errors`. A failed file stays visible with `metadata_status: failed` and its error. `unavailable` means no ffprobe was found: hashes are still useful but duration/rate metadata is absent. The CLI returns 2 for an empty catalogue, any failed file or directory scan error, after saving the report. It returns 1 for an operation-level failure such as refusing to overwrite an existing report. Use a new output filename when retrying.

The candidate extension list includes common camera, video, audio and image extensions. **Being listed does not certify a codec or camera format.** Each ffprobe build has its own format support; inspect the actual result. Unknown extensions and symlinks are reported as skipped. Test additions against real format samples before promising compatibility.

## Data processing

The bundled helpers use local files and make no network calls. AI agent/model and connected-tool operations follow your chosen provider, configuration and permissions. This package does not establish that all subsequent analysis runs locally. Photos, booking emails and cloud review are optional.

Unreadable directories appear in `scan_errors` and `summary.scan_failed`; their contents could not be counted. The CLI returns 2 and preserves the visible records instead of silently reporting a complete inventory.
