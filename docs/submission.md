# ChatGPT plugin submission

Prepared as a **skills-only, desktop-required** package. The portable `plugin.json` declares `extensions.com.openai.requires_local_executor: true`. It bundles no MCP server and no lifecycle hooks. The GitHub release and public ChatGPT directory listing are independent.

1. Build the ZIP with `python3 tools/package_release.py --output /path/to/new-release-directory`.
2. Open https://platform.openai.com/plugins using the publishing account.
3. Select the organization/project and verified developer identity. Organization owners can submit; other members need Apps Management Write. Identity verification must be completed by the publisher.
4. Upload `family-travel-editor-plugin-v0.1.0.zip` as a new plugin. Inspect the actual metadata/skill validation findings and resolve them before submitting.
5. Review the displayed publisher and listing. Submit when the portal permits it. Approval and actual publication are separate states.

Prepared listing: **Family Travel Editor** / **Edit your travel stories**. Publisher: Denis Kortunov. Required local tools and experimental limitations are in the manifest and README. The logo is an original vector icon.

No application ID, verification, dashboard upload, review approval or publication is claimed by the presence of this document. The package has not passed live Resolve import testing. Do not hide that limitation in the listing or reviewer material.

If a local MCP server is added later, eligibility and review requirements change; current OpenAI documentation limits local MCP submissions to approved partners. That restriction is distinct from this skills-only package.

Sources checked 26 October 2026:
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/desktop-only
