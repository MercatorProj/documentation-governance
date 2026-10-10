# Documentation Governance Skill

Version: `1.0.1`

A reusable skill for organizing project documentation, maintaining code/documentation traceability, validating quality, and delivering a VitePress site for local viewing and offline distribution.

## Default operating policy

- Establish a consistent documentation system; directory restructuring is allowed when planned.
- Provide local VitePress preview and static/offline delivery.
- Detect code/documentation differences and propose changes; semantic updates require review.
- Confirm major file moves, deletion, overwrites, dependency installation, and site-config replacement before execution.
- Run checks manually; no Git hooks, CI/CD, scheduled automation, or online publication by default.

## Package contents

```text
 documentation-governance/
 ├── SKILL.md
 ├── README.md
 ├── references/
 │   ├── documentation-taxonomy.md
 │   ├── metadata-and-authority.md
 │   ├── migration-safety.md
 │   ├── code-sync-method.md
 │   ├── vitepress-delivery.md
 │   └── quality-checks.md
 ├── workflows/
 │   ├── onboarding.md
 │   ├── inventory.md
 │   ├── migration.md
 │   ├── code-sync.md
 │   ├── site-delivery.md
 │   └── audit.md
 ├── scripts/
 │   ├── inventory_docs.py
 │   ├── check_doc_links.py
 │   ├── check_frontmatter.py
 │   └── check_governance_map.py
 ├── templates/
 │   ├── docs-governance.example.yml
 │   ├── migration-plan.md
 │   ├── audit-report.md
 │   └── document-template.md
 └── examples/
     ├── sample-docs-map.yml
     └── sample-report.md
```

## How to use

1. Install/copy this directory into the skill discovery location used by your agent environment.
2. Invoke the skill for a task such as “inventory the current docs”, “plan a documentation restructure”, “compare docs with code changes”, or “build an offline VitePress site”.
3. For a new project, run the onboarding workflow. It first inspects the repository and asks only for decisions that cannot be inferred safely.
4. Run scripts manually from the repository root or pass the relevant directory explicitly. They are read-only unless documented otherwise.

## Script examples

```bash
python scripts/inventory_docs.py . --out docs-inventory.csv
python scripts/check_doc_links.py docs
python scripts/check_frontmatter.py docs
python scripts/check_governance_map.py .governance/docs.yml
```

The scripts use Python's standard library. The link checker focuses on local Markdown links and assets; it is not a full Markdown renderer or a replacement for VitePress build validation.

## VitePress delivery

The skill inspects existing package managers and site configuration before proposing changes. It does not blindly replace an existing site. The default delivery sequence is:

1. Preview locally using the repository's existing scripts or package manager.
2. Run a production build.
3. Review build output and local assets/links.
4. Optionally create an offline archive of the static output and include a short README.
5. Verify archive contents and document known limitations.

Static output can be served from a local HTTP server. Do not assume that opening `index.html` directly via `file://` will work: SPA routing, module loading, and asset paths may require HTTP serving or a VitePress base-path configuration.

## Design limits

This skill does not make product decisions, approve requirements, refactor business logic, or guarantee semantic equivalence between code and prose. It provides traceability, evidence-based drift detection, recommendations, mechanical validation, and a review workflow.
