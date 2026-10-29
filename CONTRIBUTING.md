# Contributing

Start with a question, a confusing step, or a small improvement. Use the [help and first-use template](https://github.com/denyakortunov/family-travel-editor/issues/new/choose) if you do not have a code change. Include the skill version and what you expected to happen.

Start with a small reproducible result. Describe the user task, editor/version/platform, what already works and what remains unverified. Use synthetic or explicitly redistributable footage; do not upload private paths, credentials, bookings or family source media.

For helper changes run `python3 -m unittest discover -s tests -v`. Media smoke tests use FFmpeg and ffprobe and skip explicitly when unavailable. For adapters, XML generation alone is not a successful native import: show opening, relinking, playback and an actual render. Preserve previous project versions and test away from active editing projects.

Keep narrative scene plans independent of editor APIs. Do not add provider subscriptions as universal requirements. Submit a focused pull request with validation evidence and limits.

## Checking the first-use experience

Ask a new reader to explain what the product is, try the quick start, find the resulting plan and resume in a fresh chat. Record the step where they stop and what they expected. Synthetic fixtures test code; they do not replace observation of real users. Do not post personal footage or invite others on the maintainer’s behalf without authorization.

## Publishing a version

Update `plugin.json` and `skills/family-travel-editor/VERSION` together, write `docs/whats-new-vVERSION.md`, update the release index and validation record, and test both archives. A push to main publishes a missing version only after the Python 3.9/3.12 helper/media suite passes. The release targets the tested commit, includes checksums and never replaces an existing release or moves an existing tag. Keep a version stable once published; corrections need a new version. Pull requests run tests without release permission.
