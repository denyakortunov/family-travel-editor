# Final Cut Pro on Mac

Use Final Cut Pro when the user wants an editable Mac timeline. This is an optional FCPXML workflow with a separately installed MCP server, not a bundled editor or a guarantee of unattended export.

## Start

1. Confirm Final Cut Pro is installed and licensed or in its trial period. A subscription is not specifically required for XML interchange; the one-time-purchase edition also supports it.
2. Keep media and a dedicated test library on local storage. Discover existing libraries read-only; do not import into the user's current film by default.
3. For programmatic assembly, install and connect the third-party [FCP MCP Server](https://github.com/DareDev256/fcp-mcp-server). It requires Python 3.10+; FFmpeg and ffprobe are needed for its previews. This skill's Python 3.9 helpers do not supply those dependencies.
4. Build a short test through MCP, import into the explicitly named library, and verify the project in Final Cut. Then continue in the editor or through versioned XML revisions.

With `uv` installed, an MCP client can launch the server as follows. Replace the projects directory with the user's actual workspace and keep a recorded, tested server version.

```json
{
  "mcpServers": {
    "fcpxml": {
      "command": "uvx",
      "args": ["fcp-mcp-server==0.30.0"],
      "env": {"FCP_PROJECTS_DIR": "/absolute/path/to/film-workspace"}
    }
  }
}
```

This is a client configuration example, not a command to paste into a terminal. Use the host's supported MCP settings. First use may require macOS Automation permission to communicate with Final Cut. No separate AI generation service is required for local XML assembly.

## Assembly and revision

- `generate.import_edl_json` can build FCPXML from a source map and ordered source ranges. Supply the intended frame rate and check canvas size; the tested action defaults to 1920×1080.
- `inspect.list_clips`, `edit.trim_clip` and `edit.add_audio` provide inspection, bounded trims and connected audio. Use new output paths and hash guards where available.
- `deliver.push_to_fcp` sends the XML using an Apple event. Always specify `library_location` and verify the imported project. A delivered event alone is not proof of import.
- If the user edits in Final Cut, use File → Export XML to bring those changes back before further agent edits. The tested MCP route does not provide native XML export or a complete native movie-export workflow.
- Without MCP, the agent can prepare valid FCPXML for File → Import → XML. The repository's `timeline.py` emits older FCP 7 XML (`xmeml`) for Resolve; it does **not** generate modern Final Cut Pro FCPXML. Do not give that file to the user as a Final Cut project.

## Verified scope and current limitations

On 4 November 2026, Final Cut Pro Creator Studio 12.4 on an Apple Silicon Mac accepted a three-clip synthetic project generated through FCP MCP Server 0.30.0. A second MCP revision trimmed the middle source and added a separate stereo audio bed. Read-back from Final Cut confirmed a 12-second baseline and an 11-second revision, both at 25 fps, in separate test libraries. Existing film libraries were not edited.

Two issues appeared in the third-party preview path: its MP4 output used 24 fps for this 25 fps project, and the trim left the XML sequence duration at 12 seconds even though the clips and native Final Cut timeline ended at 11 seconds. The preview consequently retained the longer duration. Check clip endpoints, sequence duration and the imported timeline; do not accept the preview's own duration check as independent proof. These upstream behaviors are not fixed by installing this skill.

Native movie export, a save/reopen round trip, native audio playback/mix quality, effects and a complete travel film were not certified in this trial. The FFmpeg preview is an external approximation, not a Final Cut export. Use native export and actual viewing/listening before delivery.

[Apple: XML interchange](https://support.apple.com/guide/final-cut-pro/use-xml-to-transfer-projects-verdbd66ae/mac) explains import and export. [FCPXML reference](https://developer.apple.com/documentation/professional-video-applications/fcpxml-reference) defines the format. Confirm the installed versions and tool schemas before use.
