# Migration safety and approval gates

## Classify change risk

### Low risk
- Add a new document or index without overwriting existing content.
- Fix a clearly broken local link when the target is unambiguous.
- Generate a report to a confirmed output path.

### Medium risk
- Change navigation order or metadata across several files.
- Rename a small number of files with fully understood references.
- Change VitePress configuration additively.

Present the proposed changes and seek confirmation when user intent is not explicit or when the result is hard to reverse.

### High risk / approval required
- Bulk move or rename documents.
- Delete, overwrite, consolidate, or replace existing documents.
- Choose between conflicting requirements or design documents.
- Replace `.vitepress/config.*`, package manifests, lockfiles, or build scripts.
- Add dependencies or change the site's public/base path.
- Package files for an audience whose access scope is unclear.

## Required migration plan

1. Inventory source paths and file types.
2. Propose `old path → new path` mappings and explain why.
3. Identify inbound/outbound links, images, imports, navigation entries, anchors, and generated references.
4. Identify collisions and files whose purpose/authority is uncertain.
5. State backup/rollback approach. Prefer Git diff and a dedicated commit/branch over ad-hoc destructive operations.
6. Ask for approval before high-risk changes.
7. Move files in bounded batches; update references with exact-target resolution.
8. Run link, asset, metadata, navigation, and site-build checks.
9. Report unresolved references and the exact paths affected.

## Collision policy

Never silently overwrite. If the destination exists, compare content and references; recommend merge, keep-both, replace, or archive, and ask for a decision.

## Git safety

- Inspect `git status --short` before editing when Git is available.
- Preserve unrelated staged and unstaged changes.
- Never run destructive cleanup/reset commands as part of documentation governance.
- Do not create a commit unless requested.
- A migration map should record old path, new path, action, reason, references updated, and validation result.
