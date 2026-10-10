# Documentation taxonomy and layout

## Goals

Make documentation discoverable without imposing unnecessary structure. Choose categories based on project size and audience, and avoid creating empty folders merely to match a template.

## Suggested information architecture

```text
docs/
├── index.md                 # landing page
├── guide/                   # user/product or workflow guides
├── requirements/             # approved product requirements when suitable
├── architecture/             # system context, components, deployment, data flows
├── api/                      # API and integration references
├── development/              # setup, conventions, debugging, contribution
├── operations/               # release, deployment, recovery, troubleshooting
├── decisions/                # ADRs and important technical decisions
└── reference/                # glossary, configuration, generated references
```

This is a starting point, not a mandatory tree. For a small library, a single `guide/` plus `reference/` may be enough. Existing project conventions and audiences take priority.

## Storage, knowledge, navigation

Keep these concepts distinct:

- Storage: where files physically live.
- Knowledge model: which concepts and artifacts relate to one another.
- Navigation: how readers reach content in the site.

A document may have one canonical file and several links from different navigation paths. Avoid duplicate copies used only to appear in multiple sections.

## Classification rules

Classify by primary purpose, not filename alone:

- Product/requirements: goals, user needs, acceptance criteria, business rules.
- Architecture/design: components, boundaries, dependencies, data flows, trade-offs.
- API/contracts: request/response shapes, events, schemas, error semantics.
- Development: setup, local workflows, coding conventions, test strategy.
- Operations: deploy, configure, observe, recover, troubleshoot.
- Decision records: context, options, decision, consequences, status.
- Project management: plans and status reports; retain only when they remain useful project records.
- Scratch/temporary: unapproved or short-lived material; do not publish by default.

## Naming

- Prefer stable, descriptive, lowercase kebab-case paths for new English-named files; preserve established language conventions in existing repositories.
- Avoid names such as `new.md`, `final-v2.md`, `latest-final.md` without contextual meaning.
- Use dates in filenames only for inherently dated records (meeting notes, releases, periodic reports).
- Do not rename files solely for stylistic consistency if links and history costs outweigh benefits.

## VitePress rules

- `docs/index.md` is the preferred landing page when `docs/` is the configured source directory.
- Navigation and sidebar configuration should be explicit and readable. Generate only repetitive portions; keep editorial ordering and curated landing pages under human control.
- Never expose secrets, private operational details, or internal-only material in a public/offline package intended for broader distribution.
- Store public assets under the configured public/assets convention and use stable relative links where possible.
