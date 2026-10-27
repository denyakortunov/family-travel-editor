# From a family trip to a film: the workflow behind this skill

I shoot family trips on a DJI Osmo Pocket 3 and drones. The footage is easy to accumulate; finding time to turn it into a story is harder. A film usually costs me 20–30 hours of editing. I cannot honestly claim the agent has made that faster yet. The useful change is that corrections can become a reusable editing process instead of disappearing into a chat.

## Start with footage and recover the context

I give the agent access to the camera and drone clips. It catalogues the files, then examines candidate material in motion. A transcript helps find a conversation, but it cannot tell whether a gesture finishes or a cut feels abrupt. Photo GPS helps identify where a scene happened; selected hotel and transport bookings help reconstruct the order of the trip. These are clues, not a substitute for asking me. Some trips were filmed years ago, so the questions often bring back the detail that makes a scene worth keeping.

We separate what is visible, what the metadata suggests and what I actually remember. The agent uses that context to propose scenes and draft voiceover in my voice. I record the narration. It should not invent an anecdote to fill a gap in the footage.

## Build scenes, then check the actual film

My own setup uses DaVinci Resolve, Python and FFmpeg. The editing rules cover complete thoughts, meaningful motion, reactions and the relationship between a scene's setup and ending. Music should support the scene. A nice-looking shot is not enough reason to interrupt a conversation.

The agent's ability to handle audio depends on the model and tools available. In my workflow, separate transcription and audio-analysis tools provide evidence when the main agent cannot listen directly. Whisper, GigaAM and other models have been used for different checks; Gemini and an optional Claude audit can add another opinion. None replaces checking the actual export, and a failed external review must remain visibly incomplete.

Review happens through timecoded comments in Replay or in chat. Each comment refers to a particular version. We preserve the earlier timeline, record what may change and protect the surrounding material. A change can be applied, checked and still not accepted by me. Repeated preferences go into project memory; a one-off cut remains attached to its scene. This is stored context, not training the model's weights.

## Watch concrete examples

[The published Bali film](https://www.youtube.com/watch?v=hzqUOtD2AqU) is 22 minutes 37 seconds. Here are three changes recorded during its final revision:

| Watch | Author's correction | What had to remain intact |
|---|---|---|
| [00:24 — airport sequence](https://www.youtube.com/watch?v=hzqUOtD2AqU&t=24s) | Keep a quiet music bed continuous through the airport sequence up to the map | The map sound and hotel music |
| [10:41 — pool drone shot](https://www.youtube.com/watch?v=hzqUOtD2AqU&t=641s) | Shorten the drone shot from six seconds to three and choose a better source range | Shift later scenes by three seconds; do not overwrite them |
| [18:17 — kayaking](https://www.youtube.com/watch?v=hzqUOtD2AqU&t=1097s) | Replace two unstable shots with steadier views of the same combined duration | Water, music and the complete later conversation on shore |

These links show the final result, not a before/after comparison. The timings and revision descriptions come from the author's production record. The film demonstrates the larger personal workflow, including manual decisions and project-specific tooling. It does not prove that a fresh installation of this public package can reproduce the whole film automatically.

## Finish and carry the learning forward

The final export is checked separately from the timeline. The project remains editable, earlier versions stay recoverable, and the author approves publication. Titles, description, chapters and thumbnail are prepared for YouTube; upload and playback quality need their own verification. A successful local render is not proof that viewers received the right file.

The public skill extracts the portable parts of this process: a catalogue, questions, scene plan, voiceover guidance, bounded changes, checks and versioned feedback. Its starter scripts cover a much narrower technical slice. Use the [synthetic example](../examples/story-to-cut/README.md) to reproduce that slice, and the [editor guide](../skills/family-travel-editor/references/editors.md) to choose your tools.
