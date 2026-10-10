# Workflow: documentation audit

## Goal
Assess documentation quality and synchronization without overclaiming semantic certainty.

## Steps
1. Define scope, exclusions, and expected standard.
2. Run available deterministic checks: inventory, links/assets, frontmatter, mapping validity, and VitePress build when applicable.
3. Review high-value pages for stale claims, contradictions, missing context, weak navigation, untested examples, and unclear authority.
4. Compare relevant docs against mapped code/spec sources.
5. Classify findings by severity: error, warning, review, info.
6. Produce a prioritized report with evidence, affected paths, impact, recommended fix, and whether approval is required.
7. Do not fix every issue automatically. Ask before major changes; apply only requested or clearly authorized low-risk fixes.

## Exit criteria
Report the scanned scope, commands run, pass/fail/not-run statuses, unresolved decisions, and next recommended actions.
