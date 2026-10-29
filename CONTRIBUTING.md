# Contributing

## Publishing a version

Update `plugin.json` and `skills/family-travel-editor/VERSION` together, write `docs/whats-new-vVERSION.md`, update the release index and validation record, and test both archives. A push to main publishes a missing version only after the Python 3.9/3.12 helper/media suite passes. The release targets the tested commit, includes checksums and never replaces an existing release or moves an existing tag. Keep a version stable once published; corrections need a new version. Pull requests run tests without release permission.


Start with a small reproducible result. Describe the user task, editor/version/platform, what already works and what remains unverified. Use synthetic or explicitly redistributable footage; do not upload private paths, credentials, bookings or family source media.

For helper changes run `python3 -m unittest discover -s tests -v`. Media smoke tests use FFmpeg and ffprobe and skip explicitly when unavailable. For adapters, XML generation alone is not a successful native import: show opening, relinking, playback and an actual render. Preserve previous project versions and test away from active editing projects.

Keep narrative scene plans independent of editor APIs. Do not add provider subscriptions as universal requirements. Submit a focused pull request with validation evidence and limits.
