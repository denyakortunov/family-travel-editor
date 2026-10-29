# What's New in v0.3.0 — a clear first run and stronger editing checks

Released 29 October 2026. This release includes the unpublished 0.2.0 work and the workflow improvements made since the original v0.1.0 release. There was no published v0.2.0 GitHub Release; we have not retroactively presented one as shipped.

## Start here

Download **family-travel-editor-source-v0.3.0.zip**, unzip it and follow [Getting started](https://github.com/denyakortunov/family-travel-editor/blob/v0.3.0/docs/getting-started.md). The source ZIP includes installation tools, documentation and the optional synthetic test. The plugin ZIP is for compatible local plugin clients; it is not a marketplace listing. SHA256SUMS.txt identifies the exact packages.

## Added

- A visible onboarding guide: which ZIP to choose, installation or direct use, first prompt, expected files, troubleshooting, updating and rollback.
- A first-run procedure inside the installed skill: explain actual capabilities, reuse information already supplied, check installation and provide one concrete next step. Later sessions resume project status rather than restarting setup.
- A standalone installation self-test. It checks templates, catalogue creation, XML ranges, source preservation and overwrite refusal in temporary storage, without personal footage, an editor, FFmpeg or network access.
- Version and installation path in the doctor output; clearer post-install instructions. A release-pinned skills CLI command for compatible agents, alongside the Python installer.
- Detailed camera-motion review: selected ranges and handles, phases/reversals, purposeful movement, all visible layers and the actual export. Optional local measurements/classifiers require representative controls; the release does not bundle those models.
- All-track preservation guidance: allowed changes, before/after snapshots, ripple alignment, nested processing, complete sound-component inventory and comparison of the actual exports.
- Scene-based music guidance: expressive montage and complete live speech, stable dialogue beds, intentional musical endings, licensed track selection and full sound-effect tails.
- Release automation after the helper/media tests: versioned source/plugin ZIPs, checksums and matching release notes. Existing releases are not overwritten.

## Changed

- Visual coverage comes before dialogue selection. Non-speech action, beauty, scale and atmosphere are legitimate editorial material; a shot does not need a new factual claim.
- Repetition is judged by scene function, not only source frames or a different crop. Expressive views can develop a place together; exhausted views should not fill a duration target.
- Local audio checking separates ASR, signal measurements, narrowly validated model tasks and actual listening. Known controls limit model claims, and unverified acoustic aspects remain explicit.
- Feedback status and work queue are separate: applied/verified is not accepted; historical unresolved comments do not automatically become new assignments.
- Handoffs explicitly cover one live editor, per-machine media paths, local databases/cache, versioned project exports and confirmed destination sync. A DRP does not contain camera media.
- The README now directs users to an exact release download. Current Codex installation guidance uses its documented user skill location; existing installations can update in place with a backup.

## Removed or retired

- Gemini is no longer shown as part of the current originating review workflow. No cloud reviewer is required; other users retain their own explicitly chosen services.
- Removed wording that implied every attractive shot must provide new information. No fixed shot count, shot duration or montage order is imposed.
- Retired the moving main-branch ZIP as the primary beginner download. The historical workflow illustration is retained and labelled as historical.

## Included from the previously unpublished 0.2.0 work

Editor-independent planning, clearer story/technical-plan separation, the silent FFmpeg preview, task-based doctor, backup-preserving installer, synthetic examples, detailed footage-to-film documentation and helper/media tests. The repository identity remains `family-travel-editor`.

## Feedback addressed

[Issue #2](https://github.com/denyakortunov/family-travel-editor/issues/2) identified the version/release mismatch and asked for installation beyond Codex. This release provides a real tagged download, an optional skills CLI route and a standalone runtime check. The shorter About-text suggestion is separate repository metadata and is not claimed as changed here. The issue is not automatically closed.

## Compatibility and limits

No film workspace schema migration is required. Update the installed skill using the same location; the Python installer preserves the old copy outside discovery. Keep film preferences and feedback in the workspace.

The preview/XML helpers remain video-only. Full audio mixing, trained motion analysis, model downloads, native editor automation and publication are not added by this release. Resolve's native import/playback/export is still unvalidated. The draft Shotcut adapter is not merged or included. Installation tests do not prove app discovery, editorial quality, or a complete autonomous film. See [validation coverage](https://github.com/denyakortunov/family-travel-editor/blob/v0.3.0/docs/validation.md).
