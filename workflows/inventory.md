# Workflow: documentation inventory

## Goal
Create a factual inventory without changing project files.

## Steps
1. Determine repository root and the directories in scope; respect ignore/exclusion rules.
2. Enumerate likely docs (`.md`, `.mdx`, `.rst`, `.txt`, common diagram/image assets) and relevant site config files.
3. Record relative path, extension/type, size, title if detectable, frontmatter status, likely category, and links/references if available.
4. Flag probable duplicates, vague filenames, empty files, missing landing pages, orphan pages, stale-looking drafts, and conflicting versions as hypotheses—not conclusions.
5. Sample content and inspect references before recommending moves.
6. Save or display a summary table. Write a CSV only to an agreed path.

## Output
- Counts by type/category.
- Key entry points and current site setup.
- Potential issues with evidence and confidence.
- Items requiring human interpretation.
- No file changes unless explicitly requested.
