# Workflow: project onboarding

## Goal
Establish project-specific documentation governance with minimal disruption.

## Steps
1. Inspect root structure, project instructions, Git status, current documentation, package manager, site config, and existing automation.
2. Run the inventory workflow and inspect a representative sample of files, not only filenames.
3. Identify audiences, document types, existing authoritative specs, generated docs, and sensitive/private content.
4. Draft a target layout based on the taxonomy reference. Mark optional folders and explain what each solves.
5. Propose governance config fields: doc roots, excluded paths, taxonomy, source mappings, validation commands, site root/output, delivery policy.
6. Present a short adoption plan grouped into: immediate safe fixes, proposed migrations, decisions needed, deferred improvements.
7. Ask for confirmation before major restructuring, deletions, dependency changes, or replacing site configuration.
8. After approval, implement in small batches and validate.
9. Produce a baseline report and document manual commands. Do not create hooks or CI.

## Deliverables
- Current-state inventory.
- Proposed target structure and rationale.
- Migration plan when needed.
- Project governance config, if approved.
- Validation report and local preview/build instructions.
