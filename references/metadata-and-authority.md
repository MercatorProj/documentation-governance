# Metadata, status, and authoritative sources

## Optional frontmatter for maintained documents

```yaml
---
title: Example document
summary: One-sentence description of the document.
status: active
owner: team-or-role
last_reviewed: 2026-10-10
source_of_truth: src/domain/schema.ts
review_triggers:
  - src/domain/schema.ts
  - API contract changes
---
```

Use only fields that the project actually maintains. Do not fabricate an owner or a review date. `last_reviewed` means a human or explicitly defined process reviewed the content; it must not be changed merely because a script ran.

## Status meanings

- `draft`: not approved for reliance.
- `active`: current maintained content.
- `needs-review`: likely affected, conflicting, or not yet validated.
- `deprecated`: retained for migration or historical context but should not be used for new work.
- `archived`: preserved as a record, not maintained as current guidance.

## Authority mapping

Map each information type to an explicit authority:

| Information | Possible authority | What code can prove |
|---|---|---|
| Public function signature | source/API extraction | Current symbol shape, not intended usage rationale |
| API schema | OpenAPI, JSON Schema, typed contract, or implementation | Current declared fields and types, subject to runtime validation |
| Data model | schema, migrations, types, database definitions | Current structural evidence; business meaning may need review |
| Business rule | approved requirement/domain specification | Implementation behavior, not which rule is correct |
| Architecture rationale | ADR or reviewed design document | Current dependency graph, not historical intent |
| Deployment procedure | scripts/config plus verified environment | Declared commands and settings, not success in every environment |
| Tutorial | maintained guide and runnable example | Whether the example runs in the tested environment |

A source mapping should include the claim/document, canonical source, validation method, and reviewer requirement. If two sources conflict, report both with evidence and ask for a decision.

## Generated vs human-maintained content

Generated content must identify its source and regeneration command when practical. Do not manually edit generated output unless the generator supports an override mechanism. Human-authored explanations should not be overwritten by code generation.

## Traceability

Use direct paths, symbol names, schema IDs, or stable feature identifiers where feasible. Avoid line-number references as the only trace because they are fragile. Traceability is evidence for review, not proof that prose is semantically complete.
