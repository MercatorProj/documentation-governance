# VitePress setup, local preview, and offline delivery

## Discover before changing

Inspect `package.json`, lockfiles, package manager, current VitePress version, docs source directory, `.vitepress/config.*`, theme/custom components, aliases, public assets, and existing scripts. Reuse the project's package manager and configuration where possible.

## Minimal expected capabilities

- Local preview command.
- Production/static build command.
- Readable site title, description, navigation, sidebar, and search configuration.
- Stable relative links and local assets.
- Mermaid or custom Vue components only when useful and compatible with the installed version.
- Build output directory documented in project config.

Do not replace an existing site configuration wholesale. Propose an additive patch and seek approval for significant changes.

## Local preview

Use the repository's existing package scripts first. If none exist, recommend a command compatible with the installed package manager/version, and ask before changing manifests. Report the exact command and expected local URL; do not claim a server was started unless it actually was.

## Static build

Build using the existing script or installed VitePress CLI. Check command exit status and inspect build output. Fix errors caused by this task; distinguish pre-existing errors from newly introduced errors where possible.

## Offline delivery

A static VitePress output is generally distributable as a directory or archive, but it may still rely on HTTP serving, configured base paths, or external assets. Before packaging:

1. Identify the actual output directory from config/build logs.
2. Confirm the intended audience and exclude secrets/internal-only docs.
3. Check local links and asset presence.
4. Search for remote runtime dependencies (fonts, images, embeds, APIs) and disclose them.
5. Include a README with contents, build timestamp/version if known, serving instructions, and limitations.
6. Archive only the intended output, not source secrets, node_modules, or unrelated repository files.
7. List the archive and verify it can be extracted; test serving it over local HTTP when practical.

Do not assume direct `file://` opening works. Relative base paths can require a VitePress `base` configuration and a rebuild. If truly air-gapped operation is required, verify all fonts, images, scripts, search indexes, and embeds are local.

## Publishing boundary

No online deployment, account connection, DNS, CDN, CI/CD, or upload is included by default. User authorization for local packaging is not authorization for remote publication.
