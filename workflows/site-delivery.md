# Workflow: VitePress site and offline delivery

## Goal
Make project docs readable locally and provide a tested static deliverable when requested.

## Steps
1. Inspect existing package scripts, package manager, VitePress version, source root, config, output directory, base path, custom components, and assets.
2. Reuse the existing site. If no site exists, propose a minimal configuration and directory plan; ask before material dependency/config changes.
3. Configure landing page, navigation, sidebars, local search, and links appropriate to actual docs. Avoid empty or speculative sections.
4. Preview locally using existing scripts. Do not claim success unless command execution confirms it.
5. Run production build and inspect the output path/logs.
6. For offline delivery, verify asset closure and remote dependencies, exclude sensitive/internal material, write a serving README, archive only the built output, list archive contents, and test extraction/HTTP serving when feasible.
7. Report exact commands, output paths, validation results, known limitations, and whether the deliverable was actually created.

## Offline caveats
- `file://` may not work; recommend a local HTTP server unless tested otherwise.
- Remote fonts, images, analytics, embeds, APIs, or CDN assets mean the package is not fully air-gapped.
- VitePress base paths can affect static hosting. Do not alter `base` without understanding the intended serving path.
- A successful build does not prove all routes and interactions work offline.

## Exclusions by default
No Git hooks, CI/CD, cloud hosting, upload, DNS, CDN, or online publication.
