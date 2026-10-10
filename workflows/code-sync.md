# Workflow: code/documentation drift and synchronization

## Goal
Find likely documentation impact from source changes, propose minimal updates, and validate authorized edits.

## Steps
1. Define scope from the user's request, changed files, or Git diff. If scope is unclear, ask one focused question after inspecting the repository.
2. Read source mappings in `.governance/docs.yml` or equivalent.
3. Extract concrete changes: API signatures, schema fields, config keys, commands, route definitions, module boundaries, or behavior explicitly evidenced by tests.
4. Map changes to docs and explain each relationship with file/symbol evidence.
5. Classify findings as mechanical, semantic, conflict, or unknown; assign confidence.
6. Return an impact table and proposed patch summary before semantic edits.
7. Apply approved mechanical edits if requested. Semantic edits require review; do not infer business intent from implementation alone.
8. Validate edited docs, links, examples, and site build where relevant.
9. Report handled/deferred findings and remaining uncertainty.

## Required report fields
Source change; affected document; evidence; finding class; confidence; recommendation; approval/status.

## No diff available
Do not fabricate a Git diff. Analyze the specified files/features and label the scope accordingly.
