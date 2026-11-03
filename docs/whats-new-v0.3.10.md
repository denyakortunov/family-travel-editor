# What's New in v0.3.10

4 November 2026

- Added an explicit Final Cut Pro route, with setup instructions for optional third-party MCP control and modern FCPXML interchange.
- Verified basic three-clip assembly, a middle-clip trim and connected-audio import in Final Cut Pro Creator Studio 12.4 on Apple Silicon. Native read-back confirmed 12 seconds before the revision and 11 seconds afterward at 25 fps.
- Documented the tested server's preview frame-rate mismatch and stale XML sequence duration after trimming. Native export, reopening and audio quality remain unverified.
- Clarified Resolve Free versus Studio external scripting requirements.
- Removed Shotcut from current editor recommendations and the roadmap. The experimental adapter was not shipped.

This release changes instructions and documentation. It does not bundle Final Cut Pro, an MCP server or new editing commands. CapCut native editing is not certified by this release.

[Final Cut setup and tested limits](https://github.com/denyakortunov/family-travel-editor/blob/v0.3.10/skills/family-travel-editor/references/final-cut.md) · [Capabilities](https://github.com/denyakortunov/family-travel-editor/blob/v0.3.10/docs/capabilities.md)
