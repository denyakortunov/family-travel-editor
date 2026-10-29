# Your first scene

[Download v0.3.6](https://github.com/denyakortunov/family-travel-editor/releases/tag/v0.3.6) · [What's New](whats-new-v0.3.6.md) · [Full workflow](from-footage-to-film.md)

This is a skill for a local AI agent, not a video-editing app. Installing it adds instructions and small helpers. It does not begin an edit, install Resolve, connect private accounts or download models. The helper programs need Python 3.9+ and an agent that can access your files. Text-only planning can begin without Python. ffprobe adds technical media metadata; rendering the optional silent test needs FFmpeg and ffprobe. Your agent has its own access and pricing.

## 1. Pick one installation route

### Start here: source ZIP, no global installation needed

Download **family-travel-editor-source-v0.3.6.zip** from the release and unzip it. Open the `family-travel-editor` folder in your local agent. The `README.md`, `tools/` and `skills/` folders should be visible. Ask it:

> Read skills/family-travel-editor/SKILL.md. Check this installation and explain the next step. Do not edit any film yet.

This works by reading the skill directly. No global installation is necessary. Download `SHA256SUMS.txt` beside the ZIP if you want to verify the exact package: on macOS use `shasum -a 256 <zip>`; on Linux use `sha256sum <zip>`; on PowerShell use `Get-FileHash <zip> -Algorithm SHA256`. Compare the digest for that ZIP, not for a different GitHub-generated source archive.

<details>
<summary>Optional: install permanently for Codex or other agents</summary>

### Install for Codex

From the extracted repository root:

```sh
python3 tools/install_skill.py --destination ~/.agents/skills
python3 ~/.agents/skills/family-travel-editor/scripts/self_test.py
```

The current [Codex skill documentation](https://developers.openai.com/codex/skills) lists `~/.agents/skills` for user skills. If your existing installation uses `~/.codex/skills`, update that existing location instead; avoid two installed copies with the same name. You can also choose a project-specific `.agents/skills` destination. Windows is not end-to-end tested. On Windows, use `py -3` instead of `python3` if that is how Python is installed, and pass the destination quoted as an absolute path.

Open a new chat in your film workspace and type `$family-travel-editor`. If it does not appear, restart the agent, verify the selected folder contains `family-travel-editor/SKILL.md`, and ask the agent to read that file directly. Filesystem installation checks do not establish that a particular app has loaded the skill.

### Other agents with the skills CLI

From the project where you want to use it:

```sh
npx skills add https://github.com/denyakortunov/family-travel-editor/tree/v0.3.6/skills/family-travel-editor
```

Choose your agent when prompted. This pins the skill to this release; the short repository form follows current main. The [third-party CLI](https://github.com/vercel-labs/skills) supports several agents; its current documentation requires Node.js 22.20+. The skill itself needs no Node runtime. Use the Python route if you prefer no npm dependency. The entire skill folder is self-contained; repository-level `tools/` and examples are not runtime dependencies. See [what was tested](validation.md).

The plugin ZIP is an alternative for clients supporting the repository's plugin manifest. It is not an approved marketplace listing. For a first try, use the source ZIP or skill installation above.

</details>

## 2. Confirm that it works

From the installed skill directory (the installer prints its exact location):

```sh
python3 scripts/project.py doctor --task plan
python3 scripts/self_test.py
```

Expect `plan: READY` and `PASS: family-travel-editor 0.3.2 installation check`. The check uses temporary fake metadata, validates templates and XML ranges, verifies overwrite refusal and leaves originals untouched. It uses no private media, network, editor or model. It does **not** prove playback, audio quality or editing ability.

For a separate real-render test, the source ZIP includes [color-bar fixtures and exact commands](../examples/first-scene/README.md): three shots total 12 seconds, then a middle-shot trim makes 10 seconds. Both are silent. This is a technical test, not a sample family film. For a recorded planning interaction without footage, use the [memory-to-plan session](../examples/memory-to-plan/README.md).

## 3. Try real footage or give it one scene

For a complete **picture-only** exercise, the source ZIP includes [Grand Canyon clips, previews and one command](../examples/grand-canyon-sunset/README.md). It generates a separate workspace with STATUS and plans so you can continue tomorrow. It needs FFmpeg/ffprobe and deliberately excludes audio.

With your own footage, check access from the skill directory (replace the path):

```sh
python3 scripts/project.py doctor --task catalog --source "/absolute/path/to/footage"
```


Copy this and fill in your folders:

> Use $family-travel-editor. My footage is in [folder]. Keep planning files in [a different folder]. I use [editor, or undecided]. Help me plan one scene about [moment/place]. Check your ability to inspect picture and sound, catalogue the footage and map what the scene can show before choosing dialogue. Ask only questions that affect the story. Give me a scene plan with confirmed facts, gaps and the next step before editing. Preserve the originals.

If you did not install, replace the first sentence with “Read skills/family-travel-editor/SKILL.md.” No footage yet? Ask the agent to explain the mountain-trip example without pretending it has inspected your clips.

## 4. Know what you should receive

| Output | What it means | What it does not prove |
|---|---|---|
| `catalog.json` | Files, hashes and available technical metadata | That every clip was watched |
| `scene.json` | The story, evidence, candidate ranges and gaps | A rendered or accepted film |
| `preferences.json` / `feedback.json` | Scoped preferences and versioned requests | That a request has been fixed merely by writing it down |
| `STATUS.md` | Completed work, limits, next action and any needed answer | That another computer received the files |

The agent should explain what it inspected, what it can assemble in your editor and what comes next. A full edit needs actual editor access; iMovie/CapCut/other editors can use a manual assembly plan. The bundled preview is silent, and Resolve XML remains video-only with a native round trip unvalidated. Do not let a silent preview replace your family dialogue.

## 5. Assemble, give feedback and return tomorrow

Ask for a readable table as well as `scene.json`: source file, IN/OUT, shot purpose, speech, music and the next editor action. If the agent cannot inspect the clip, it must leave ranges unselected. Use the [manual assembly example](manual-assembly.md) for an editor without an adapter. Do not pass narrative `scene.json` directly to the video renderer; the [plan formats](../skills/family-travel-editor/references/plan-formats.md) are different.

Give a bounded note such as: “In v1 at 00:04, shorten the middle shot by two seconds; preserve the opening and ending.” The agent should record the request, make v2, compare the protected material and state what was checked. It must not mark your feedback accepted merely because a command succeeded. [Complete synthetic example and saved status →](../examples/story-to-cut/README.md)

In a fresh chat, use:

> Read the installed family-travel-editor SKILL.md, then read STATUS.md, scene.json, preferences.json and the relevant feedback.json entries in [absolute film workspace path]. Continue from the recorded version and next step. Recheck source access and editor ownership if editing is needed. State what was actually verified; ask only for missing information required to continue.

Keep those files in your film workspace, not the skill's installation folder. Save the editor project and identify the corresponding review export before a handoff; shared documents alone do not transfer media or prove synchronization.

## 6. Update or undo an update

Download the new version and run the installer with the **same destination** and `--update`:

```sh
python3 tools/install_skill.py --destination ~/.agents/skills --update
```

It prints the backup location in the sibling `skills-backups` directory. Re-run the installation check and start a fresh chat. Film workspaces are not migrated or overwritten. To roll back, move the current installed copy somewhere outside discovery, then restore the printed backup to `family-travel-editor` in the original destination. Keep your own preferences in the film workspace so updates cannot replace them. If you installed through the third-party CLI, manage that copy with its commands; do not overlay a second installation.

## If you get stuck

| Symptom | What to do |
|---|---|
| Nothing happens after installation | Expected: start a chat and invoke the skill with a scene request |
| “Can't find scripts/project.py” | Use the absolute installed path printed by the installer; your film folder is not the skill folder |
| Python missing | Install Python 3.9+ or use your existing interpreter; Windows may use `py -3` |
| Empty catalogue or exit code 2 | Open `catalog.json`: `summary` reports counts, `skipped` explains exclusions and failed records explain problems. A partial catalogue is saved; retry failed files after resolving their errors, into a new output file. |
| FFmpeg missing | Planning/self-test still work; preview rendering needs FFmpeg and ffprobe |
| Existing workspace/output | Resume it or choose a new version/path; helpers refuse replacement |
| Agent cannot see/hear footage | Ask for a plan with explicit unreviewed ranges; do not accept a claimed audiovisual PASS |
| Preview has no sound | Expected for this helper; use an editor for speech/music assembly |

For a bug report include version, OS, agent, editor, command or task, expected/actual result and a small synthetic example when possible. Do not attach family footage, credentials or booking records to a public issue. [Report a problem](https://github.com/denyakortunov/family-travel-editor/issues/new/choose).

## Your data

The bundled helpers do not use the network. The AI agent and any transcription, vision or connected account tools have their own data handling and settings. Local catalogue generation does not guarantee that later model analysis stays on your computer. Photos and email are optional; selected exports or your answers are sufficient to start. [Capabilities and actual checks](capabilities.md).
