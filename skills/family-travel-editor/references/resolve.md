# Resolve operations

Release status: the bundled XML import/playback/export round trip remains unvalidated in v0.3.9. XML generation is tested separately. Production experience behind the editing instructions does not certify the bundled adapter.

## Free or Studio?

Edition requirements checked 3 November 2026. These are documentation findings, not a native-editor test certificate.

| Work with this skill | Resolve Free | Resolve Studio |
|---|---|---|
| Catalogue footage, prepare a scene plan and generate XML outside Resolve | Yes; these helpers do not require Resolve | Yes |
| Assemble the plan manually in the editor | Available editing route | Available editing route |
| Import the generated video-only XML through the editor UI | Candidate route; this package's round trip is unvalidated | Same validation still required |
| Run the bundled external Python bridge | Not supported | Requires local scripting access; a connection alone does not validate import or export |

The [official Resolve 21.1 release notes](https://www.blackmagicdesign.com/support/content/readme/59dd4eef1f4941c29fb8dc48b33f5c87) explicitly move Python scripting to Studio. Do not send Free 21.1+ users to old instructions for launching Python from the Scripts menu. Do not promise a Lua wrapper, a different MCP server or UI automation as an equivalent tested replacement for this bridge.

For a free workflow, use the [manual assembly plan](editors.md) or test XML import in a separate empty project through File > Import > Timeline. Keep the media in place, match the plan's frame rate, then check source ranges, missing media, cut positions and the exported picture. Our XML has no audio, titles or effects; add those separately. Successful XML generation is not proof that native import works.

Free supports ordinary editing and delivery up to UHD 3840 × 2160 at 60 fps. Studio adds advanced noise reduction, voice isolation and other optional tools. See [Blackmagic's edition overview](https://www.blackmagicdesign.com/products/davinciresolve/studio). Buying Studio is not required to start planning or manually editing a family film.

Check camera files against the [Resolve 21.1 codec list](https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_Supported_Codec_List.pdf) for the actual OS, codec and profile. Do not claim that all 10-bit footage requires Studio or that all H.264/H.265 acceleration is absent from Free: the macOS, Windows and Linux tables differ. Test representative camera clips before choosing a route; conversion does not resolve the scripting restriction.

## External bridge: Studio

Use the scripting documentation installed with the user's Resolve version. On macOS it is normally under `/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/`. The bundled external Python bridge requires Studio. During setup, enable Preferences > System > General > External scripting > Local. Do not expose network scripting unnecessarily.

`python3 scripts/resolve_bridge.py probe` reads version and current project only. `--modules PATH` can point to the directory containing DaVinciResolveScript.py; `RESOLVE_SCRIPT_LIB` follows Resolve's own loader. A missing connection is a capability failure, not permission to modify another project.

For the included video-only interchange example, create a NEW empty project in Resolve yourself, name it `Family Travel Editor Demo`, then:

```sh
python3 scripts/resolve_bridge.py import-xml /absolute/path/to/timeline.xml --project 'Family Travel Editor Demo'
```

The importer requires that exact currently open project, zero timelines, zero media and zero subfolders. It refuses a populated project and never creates, switches or deletes projects. Importing and saving is a mutation requested by this command. Media needs to remain where the XML points. On failure, inspect the new project; the command does not claim rollback.

For real editing, duplicate a timeline, snapshot source IN/OUT and all video/audio/title tracks, and define what may change. Verify frame-rate and source-boundary semantics with a short probe on the current version; do not assume every API uses the same inclusive end. Check Fusion duration/keys after duplication. Activate the timeline being inspected before interpreting enabled-state or audio properties.

After editing, verify all preserved tracks and corresponding rendered output, save a versioned project export and hash it. A .drp contains project data, not original media. Never change paths or library storage merely to match the example. The bundled XML helper supports only integer 24/25/30 fps, same-rate video, straight cuts and no audio/effects/titles. Other timelines require a native workflow, not silent frame rounding.

Before using AI Audio Assistant or replacing music in a timeline it has processed, read [Fairlight](fairlight.md). It is optional and needs a separate comparison of the rendered mix, including intended musical contrasts and track/bus automation.
