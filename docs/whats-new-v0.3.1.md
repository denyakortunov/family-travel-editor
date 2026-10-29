# What’s New in v0.3.1

29 October 2026 — clearer first use and more reliable catalogues.

**Family Travel Editor is a skill for your AI agent, not a standalone video editor.** This update makes that distinction visible before installation and helps you reach a useful first scene plan.

## Added

- A capability table separating file installation, local helper checks, viewing/listening and native editor access.
- A recorded agent planning trial based on a public author memory, with a provisional plan, a scoped revision and saved next step. No footage was inspected and no finished film is claimed.
- A readable manual assembly exercise: source ranges, shot roles and exact actions for a two-second trim, with a saved STATUS for continuation.
- A simpler GitHub question/first-use feedback form. Private video is not required to report a confusing step.
- Optional source-folder access checking in `project.py doctor --source PATH`.

## Improved

- The quick start now precedes the long workflow. One default source-ZIP route leads to a first prompt and expected results; permanent installation options are secondary.
- README, skill and plugin use the same name, Family Travel Editor. The current entry page uses a concise workflow description; provider-specific diagrams remain historical material.
- First-run instructions distinguish what an agent can read, run, view, hear and edit. They include a manual route, clear data-processing limits and a prompt for resuming in a fresh chat.
- STATUS templates record the version, sources/exports, evidence, remaining work, active processes and next action. Contributor help comes before release-maintainer instructions.

## Fixed

- Unreadable directories are now reported as incomplete coverage instead of being silently skipped. A per-file ffprobe timeout, invalid metadata or read failure no longer discards the whole catalogue. Successful and failed records are saved together, with reasons.
- Catalogue output lists included, skipped, failed and metadata-unavailable counts, shows hashing/probing progress and warns on an empty result. More common extensions are considered as candidates; this is not codec certification.
- Installer output uses absolute paths and the Python interpreter that actually ran it. The next step explains direct SKILL.md reading as well as Codex invocation.
- The synthetic story example now includes the STATUS file its resume prompt requires.

## Updating from v0.3.0

Download and extract the new source ZIP. From its root, run the installer with the **same destination used previously** and `--update`, for example:

```sh
python3 tools/install_skill.py --destination ~/.agents/skills --update
```

Use your existing `~/.codex/skills` destination instead if that is where your skill lives. The installer preserves the old copy in a sibling backup directory and prints its location. Keep your preferences and film files in a separate workspace; they are not overwritten or migrated. Run the printed self-test command and open a new chat. Third-party CLI installations should be updated through that CLI rather than overlaid with a second copy.

The catalogue keeps schema version 1 and the existing `files` list; `summary`, `skipped` and `scan_errors` are additive. **CLI behavior changes:** an empty catalogue, a per-file failure or a directory scan error returns exit code 2 after saving the report. Automation should inspect the saved report; do not discard it because the exit code is nonzero. A metadata-unavailable hash-only catalogue remains possible without ffprobe.

## Known limitations

The bundled preview is silent; XML preparation is video-only. Full audio mixing, native editor round trips and Windows end-to-end use are not certified. The planning trial is an agent exercise, not a novice usability study or proof of a completed travel film. An independently reproduced walkthrough with redistributable travel footage and testing with new human users remain follow-up work. No new editor integration is claimed.

[Download v0.3.1](https://github.com/denyakortunov/family-travel-editor/releases/tag/v0.3.1) · [Getting started](https://github.com/denyakortunov/family-travel-editor/blob/v0.3.1/docs/getting-started.md) · [Validation](https://github.com/denyakortunov/family-travel-editor/blob/v0.3.1/docs/validation.md)
