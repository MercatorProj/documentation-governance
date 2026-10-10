# Documentation quality checks

## Quality dimensions

1. Findability: clear title, landing page, navigation, meaningful filenames.
2. Correctness: claims match their declared authority; examples are tested where feasible.
3. Completeness: required topics/sections exist for the document type.
4. Link integrity: local documents, anchors, images, and assets resolve.
5. Maintainability: ownership/status/source mappings are clear where useful.
6. Readability: concise headings, one primary purpose per page, actionable examples.
7. Delivery: site builds, assets are present, offline limitations are disclosed.
8. Security: no credentials, secrets, private data, or unintended internal docs in deliverables.

## Severity

- `error`: a requested deliverable is broken (build failure, missing required local asset, invalid required metadata).
- `warning`: likely defect or maintainability risk (stale review date, unmapped canonical source, weak navigation).
- `review`: semantic or authority question that requires a person.
- `info`: optional improvement.

Severity depends on project policy. Do not treat every missing optional frontmatter field as an error in a legacy repository.

## Suggested gates

- Before migration completion: no known unresolved links caused by moved files; collisions resolved.
- Before offline delivery: production build succeeds; intended assets exist; remote dependencies and access scope are reviewed.
- Before declaring code sync complete: all high-confidence mechanical findings addressed or explicitly deferred; semantic conflicts recorded.
- Before declaring an audit complete: state scan scope, exclusions, tool limitations, and checks not run.

## Report honesty

Never report a check as passed if it was not run. Distinguish `passed`, `failed`, `not run`, and `not applicable`.
