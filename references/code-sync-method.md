# Code/documentation synchronization method

## Principle

Detect and explain drift; do not equate “code differs from docs” with “docs are wrong”. Determine the authority for each claim before proposing a change.

## Inputs

- User's stated change or Git diff (if available).
- Relevant source files, schemas, tests, configs, scripts, and current docs.
- Project-specific mappings in `.governance/docs.yml` or equivalent.
- Existing issue/decision/requirement identifiers where present.

## Procedure

1. Establish baseline: inspect Git status and diff; if no diff is available, use the named files or feature as scope.
2. Extract changed symbols, types, routes, schema fields, configuration keys, commands, and user-visible behavior.
3. Match those changes to docs via explicit mappings first, then links, symbol references, filenames, and semantic search.
4. Build an impact table: changed source → affected claim/doc → evidence → confidence → proposed action.
5. Classify each finding:
   - `mechanical`: path, name, field, signature, command, generated reference can be checked deterministically.
   - `semantic`: meaning, workflow, intent, acceptance criteria, architectural rationale; review required.
   - `conflict`: authoritative sources disagree; decision required.
   - `unknown`: insufficient evidence; investigate or ask.
6. Propose minimal doc edits. Separate safe mechanical corrections from semantic rewrites.
7. Apply only authorized changes; never alter business code to make documentation appear consistent unless separately requested.
8. Re-run relevant checks and list remaining findings.

## Confidence guidance

- High: exact symbol/schema/command mismatch with a direct source.
- Medium: direct linkage exists but interpretation is required.
- Low: inferred relationship based on names or broad semantic similarity.

Do not auto-fix medium/low confidence semantic findings. Explain evidence and request review.

## Drift report format

| Source change | Documentation | Evidence | Finding type | Confidence | Recommendation | Status |
|---|---|---|---|---|---|---|

## Common traps

- A code implementation may be a bug, not a new requirement.
- Tests may describe current expected behavior but may themselves be wrong or stale.
- A schema can define types without explaining business meaning.
- Generated API docs can be structurally correct but omit usage caveats.
- No detected drift is not proof of full semantic consistency.
