# Workflow: documentation restructuring and migration

## Goal
Improve findability while preserving content, links, and history where practical.

## Before editing
1. Complete inventory and inspect Git status.
2. Draft target taxonomy and `old → new` mapping.
3. Detect destination collisions and references from Markdown, config, code, images, and navigation.
4. Classify actions by risk using `references/migration-safety.md`.
5. Ask approval for bulk moves, deletion, overwrite, or unresolved canonical-source decisions.

## Execution
1. Apply a small, coherent batch of moves.
2. Update links using exact target resolution; preserve anchors where possible.
3. Update navigation and image/asset paths.
4. Record every move, merge, archive, or skipped item in the migration map.
5. Do not delete original content until the approved plan explicitly calls for it and references are checked.

## Verification
- Run local link/asset checks.
- Check navigation and frontmatter.
- Build VitePress if configured and dependencies are available.
- Inspect `git diff --stat` and relevant diffs; verify unrelated user changes remain untouched.
- Report unresolved links, ambiguous duplicates, and any checks not run.
