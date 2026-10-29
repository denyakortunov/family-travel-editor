# AI Travel Video Editor

**Turn your travel footage and half-remembered moments into a story you can edit—with an AI agent, your own voice and the editor you choose.**

[**Download & start →**](#start-with-one-scene) · [What’s New in v0.3.0](docs/release-notes.md) · [How the full workflow works](docs/from-footage-to-film.md) · [Free tools & alternatives](#choose-your-tools-and-budget)

I film our family trips on a DJI Osmo Pocket 3 and drones. Editing a film usually takes me 20–30 hours, so footage can sit untouched for years. I built **Family Travel Editor** to give an AI agent a repeatable process: inspect the material, reconstruct the trip, ask me what mattered, help plan the edit and work through my feedback. It still takes work; I am not claiming a one-click film or a proven time saving.

<picture>
  <source media="(max-width: 600px)" srcset="docs/workflow-mobile.svg">
  <img src="docs/workflow-overview.svg" alt="From footage, Photos GPS and booking emails to story, recorded narration, editing, timecoded review and approved delivery" width="960">
</picture>

The device and interface illustrations are schematic, not screenshots. The diagram retains the earlier tool examples; Gemini is retired from the current originating workflow. Follow the current checks described below. The diagram shows the **full working method behind the skill**. This repository shares its instructions and helper scripts. Which steps the agent can execute depends on its tools and access; the included renderer makes a simple silent preview.

## What happens between “here are my clips” and a film?

### 1. Reconstruct the trip from footage, photos and email

The agent catalogues camera and drone clips, inspects the available picture and sound, and builds a transcript when a speech tool is available. **Apple Photos supplies GPS, dates and nearby pictures** to help identify a place. **Selected Gmail messages supply hotel bookings and travel tickets** to reconstruct the intended route. Conflicting dates stay visible: a booking is evidence of a plan, not proof that it happened. You can provide exports or answer questions instead of connecting either account.

**You get:** a footage catalogue, a context ledger with sources, and specific questions about gaps.

### 2. Find the story—and record your own narration

Short memory clips help you remember what was happening. The agent asks questions that change the film: why did we go there, what surprised us, what happened next? Your answers become a scene plan and a narration draft. You review the words, record the voiceover and choose the takes to keep. In my setup I use a **HyperX SoloCast**; a microphone or recorder you already own is fine. Narration adds personal meaning and leaves room for the original conversations.

**You get:** a scene outline, selected source ranges, a recording script and accepted voice takes.

### 3. Assemble picture, voices, music and graphics

My working setup uses **DaVinci Resolve Studio**, Python scripts and Fairlight for audio. The edit includes speech and atmosphere, music and sound effects, titles, maps and color. Keep complete thoughts and reactions, remove camera searching and avoid repeating scenery just to fill time. Check that each shot adds something to the scene.

**The editor is replaceable.** The shared plan works with iMovie, CapCut or an open-source editor. Assembly can be manual where an adapter is missing. This package includes an **FFmpeg silent-preview renderer** and video-only Resolve XML preparation; its native Resolve round trip still needs validation. It does not supply automatic audio mixing or an adapter for every editor.

### 4. Watch an export, leave timecoded comments, revise

I review versions in **Dropbox Replay** and comment on the actual moment: “the camera turns away here,” “keep the whole answer,” or “the aircraft sound disappeared.” The agent turns those notes into a bounded change, saves a new version and compares what should have stayed intact. Plain text with **version + timecode + request** works too.

Checks use different tools for different jobs: **Whisper / GigaAM** for speech; **FFmpeg** for decoding and signal measurements; locally tested models for narrowly scoped audio/motion questions; **Claude** for an optional editorial second opinion. Gemini review was retired from my workflow; no cloud reviewer is required. These are examples from my setup, not bundled services or guarantees. A transcript is not listening; I still watch and listen to the film.

### 5. Approve, deliver and keep useful memory

After approval, prepare the final export, thumbnail, description and chapters for **YouTube or another destination**. Check the uploaded result. Keep the scene decisions, accepted recordings, explicit preferences and unresolved feedback in project files so the next session can continue. A comment about one shot stays attached to that version; it does not become a rule for every film. The repository does not automatically publish videos.

[Full workflow, evidence and handoffs →](docs/from-footage-to-film.md) · [Historical tool map](docs/workflow.png) (older services shown; current checks are described here)

## A concrete story: why the sweaters, tea and fireplace matter

One useful question from my workflow was **why we went to the mountains**. My answer: we wanted cooler weather than we get in Singapore. That gives the sweaters, tea and fireplace a shared meaning. The scene can show what we were looking forward to and what the place felt like, instead of becoming an unrelated collection of pretty shots.

| Material or answer | How it changes the work |
|---|---|
| Photo GPS, dates and selected booking records | Establish a likely place and travel order; flag anything that conflicts |
| “We wanted a break from Singapore’s heat” | Give the scene a motivation, confirmed by the person who was there |
| Sweaters, tea and fireplace moments | Look for shots that express that experience, then verify their actual content |
| A narration draft in my own words | Explain the personal reason without talking over the original conversations |
| A comment on the exported scene | Revise that moment and preserve the surrounding speech, music and reactions |

This is a **planning example based on an actual author answer**. The edit structure is illustrative; no finished film is presented as an automatically generated result. [Follow the example from evidence to recording and review →](docs/from-footage-to-film.md#a-worked-story-example-a-break-from-the-heat).

## Start with one scene

1. **[Download v0.3.0 source ZIP](https://github.com/denyakortunov/family-travel-editor/releases/download/v0.3.0/family-travel-editor-source-v0.3.0.zip)** and unzip it. Open the folder in a local agent. This is an Agent Skill, not an app; installation alone does not start an edit.
2. **Check the installation.** Ask: “Read `skills/family-travel-editor/SKILL.md`, check this installation and explain the next step.” The included self-test needs Python 3.9+, no footage, editor or paid service.
3. **Start your scene.** Give the agent a footage folder, a separate planning folder, your editor (or “undecided”) and the moment you want to tell. Expect a catalogue, scene plan and a status note before moving to assembly.

[**Step-by-step installation, first prompt, expected results and troubleshooting →**](docs/getting-started.md)

To install for current Codex versions, run from the extracted repository root:

```sh
python3 tools/install_skill.py --destination ~/.agents/skills
```

Open a new chat and invoke `$family-travel-editor`. Existing `~/.codex/skills` users should update their existing location, avoiding duplicate copies. The [guide](docs/getting-started.md) covers verification, updates with backups, Windows and direct use without installation.

For other compatible agents, the optional [skills CLI](https://github.com/vercel-labs/skills) can install this release:

```sh
npx skills add https://github.com/denyakortunov/family-travel-editor/tree/v0.3.0/skills/family-travel-editor
```

Choose your agent when prompted. The CLI needs Node.js; the Python installation route does not. [Test coverage and limits](docs/validation.md).

**Want to understand the workflow first?** Follow the [worked story example](docs/from-footage-to-film.md#a-worked-story-example-a-break-from-the-heat). The separate color-bar trimming test below verifies timing, not storytelling.

## Choose your tools and budget

The skill and its helper scripts are **free and open source**. A paid Resolve license is not required to start. Use the services you already have; the agent and any cloud models may have their own charges.

| Job | Example tool | Cost / practical alternative |
|---|---|---|
| Organize the workflow | Codex or another compatible local agent | Agent plan/API charges depend on your setup; skill files are free |
| Catalogue and render a test preview | Python + [FFmpeg](https://ffmpeg.org/legal.html) | **Free / open source**; preview helper included |
| Recover places and travel context | Apple Photos, Gmail | Optional existing accounts or selected exports; your answers also work |
| Edit a film | [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) | **Free edition available; Studio paid.** My external scripting setup targets Studio |
| Use an open-source editor | [Shotcut](https://www.shotcut.org/) / [Kdenlive](https://kdenlive.org/about/) | **Free / open source.** Plans work now; native adapters need separate validation |
| Use an editor you know | [iMovie](https://apps.apple.com/us/app/imovie/id408981434) / CapCut | iMovie is **free on supported Apple devices**; CapCut features/plans vary. Manual assembly in this package |
| Record narration | Your microphone + [Audacity](https://www.audacityteam.org/) or an existing recorder | Audacity is **free / open source**; no specific microphone required |
| Transcribe speech locally | [Whisper](https://github.com/openai/whisper) | **Open source**; local hardware required. Hosted transcription may charge |
| Review with timecoded comments | [Dropbox Replay](https://help.dropbox.com/create-upload/dropbox-replay-faq) | **Limited access included with Dropbox plans**; paid options. A text feedback file is free |
| Get a second opinion | Human review, optional editorial reviewers | **Optional**; access and charges vary. Human review remains essential |

Cost categories checked against linked product sources on 27 October 2026; limits and plans can change. Tools are optional examples, not accounts or subscriptions bundled with the skill. [Editor capabilities and integration limits](skills/family-travel-editor/references/editors.md).

<details>
<summary><strong>For contributors: automated trimming test (color bars, no travel footage)</strong></summary>

The repository includes an intentionally artificial FFmpeg test fixture. Its clips contain **animated color bars**, with no people, speech or music. They check that a two-second trim changes only the selected shot and preserves the surrounding source ranges.

This is a software verification test, not a sample travel film or a preview of the skill's creative output. Keep it separate from the [story and editing workflow](docs/from-footage-to-film.md).

[Technical test instructions and files](docs/walkthrough.md) · [Recorded validation](docs/validation.md)

</details>

## What is included—and what needs your setup

This is an **Agent Skill**, not a standalone video editor. Included: workflow instructions, project templates, catalogue and measurement helpers, a silent-preview renderer, video-only XML preparation and reproducible examples. Full audio mixing, graphics, native editor control, connected account access and publication require appropriate tools. [Validation](docs/validation.md) · [Roadmap](docs/roadmap.md) · [Release notes](docs/release-notes.md).

Start with one scene. If something breaks, [report your editor, the task and the observed result](https://github.com/denyakortunov/family-travel-editor/issues/new/choose). If you build an adapter, include a small reproducible example and evidence of import, playback and export. [Contribution guide](CONTRIBUTING.md).

Original code and instructions: [MIT](LICENSE). [Third-party notices](THIRD_PARTY_NOTICES.md). Independent project; not affiliated with the editors or services shown.

Created by [Denis Kortunov](https://github.com/denyakortunov).
