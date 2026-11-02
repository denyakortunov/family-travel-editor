# Optional music library: Epidemic Sound

Use this only when the filmmaker chooses Epidemic Sound. Otherwise continue with their existing licensed library or a music brief. No subscription, credentials or MCP server is bundled with this skill.

## Connect and check

The [official MCP guide](https://developers.epidemicsound.com/docs/mcp/) was checked on 2 November 2026. Server: `https://www.epidemicsound.com/a/mcp-service/mcp`. Follow that guide for the user's client and account. MCP credentials differ from Developer Portal API keys. Keep credentials outside the skill, film workspace and shared reports.

Discover the tools actually exposed in the current session. A saved configuration is not a working connection. Without access, use the website manually or leave a concrete selection brief; do not imply a search or download happened.

## Select, then use

1. Start from the scene's role and the filmmaker's reference. `SearchExternalReferences` finds reference IDs; use a returned ID with `SearchRecordings` through its `externalID` parameter. Read the current tool schema rather than guessing arguments. Reference similarity is a lead, not a selection decision.
2. Listen to the candidate's entire intended range, then in the scene. Check competing vocals, changes of energy, speech space and the ending using [scene music](scene-music.md). BPM and mood tags cannot establish fit. Record selection/rejection reasons; mark listening as incomplete when unavailable.
3. Download the chosen recording with `DownloadRecording`; original-track stems are an option when needed. Store media in the filmmaker's media folder. For object sounds, use `SearchSoundEffects` and `DownloadSoundEffect`, then verify the actual attack and picture contact.
4. Record title/creator, recording ID, source, chosen range, local file and the applicable license evidence. Confirm coverage for the intended account/channel and publication; a successful download does not settle those rights. Never include downloaded licensed tracks in a public skill package.

Free accounts can search/preview; downloads need a paid subscription. Check the account's actual terms and available features. Do not buy or upgrade a plan merely to complete a search.

## Optional track adaptation

After selection, `EditRecording` → `PollEditRecordingJob` → `DownloadRecordingEdit` adapts a track. Check availability and cost before starting. If polling is unavailable, do not start an unretrievable job or keep submitting duplicates. Current documented limits include a five-minute maximum and full-mix edits; obtain stems from the original recording. Review the resulting edit's musical seams and scene timing before use. Respect retry delays and stop on a failed job rather than treating it as a completed download.
