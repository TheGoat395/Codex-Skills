# Skill Quality Standard

This repository treats Codex skills as public workflow infrastructure. A skill should make Codex more reliable in a specific situation, not merely add another style preference.

## Required Metadata

Each skill must include frontmatter in `SKILL.md`:

```yaml
---
name: example-skill-name
description: Use this skill when...
---
```

Use the shortest description that distinguishes the actual trigger. There is no minimum prose length. Avoid broad keyword inventories, duplicated ownership and catchall language that attracts unrelated tasks. Judge correct selection with representative positive and negative cases; a metadata check alone cannot prove it.

## Acceptance Criteria

A skill is acceptable when it:

- has a narrow, recognizable trigger
- produces concrete behavior or decisions
- names verification steps where relevant
- avoids broad claims like "make it better" without instructions
- respects project-local dependencies
- avoids hidden destructive actions
- avoids private tokens, credentials, personal data, and non-public links
- includes fallback behavior for missing tools, missing assets, or blocked access
- says when to ask the user instead of inventing context

## Public Repo Criteria

Before a skill is added to this public pack, check that it:

- contains no private workspace paths except generic examples
- contains no account-specific secrets or internal-only instructions
- does not encourage bypassing access controls or platform rules
- does not require paid or private services unless clearly optional
- can be understood by someone who did not write it
- improves one of the repository collections or fills a documented gap

## Review Checklist

Use this checklist for pull requests:

- Metadata is valid and the description is trigger-focused.
- The skill has a clear purpose and does not duplicate an existing skill without improving it.
- Instructions are operational, not just adjectives.
- Any tool use is bounded and honest about permissions.
- Any code-changing workflow includes verification and rollback thinking.
- Any frontend workflow includes rendered QA and responsive polish expectations.
- Any research workflow uses public, authorized, or user-provided sources.

## Rejection Criteria

Reject or rewrite a skill when it:

- exists mainly to increase the skill count
- uses generic taste language without concrete choices
- overlaps heavily with a stronger existing skill
- adds global dependency installation as a default
- implies guaranteed output quality
- hides risk from users
- contains private data, credential material, or account-specific instructions

## Instruction delivery

Assume a capable model. Preserve non-obvious domain knowledge, task boundaries, required formats and meaningful verification; remove generic encouragement and unnecessary itineraries. Keep shared invariants and workflow selection in the root. Move substantial conditional procedures to linked references with explicit read conditions. Simple skills need no extra routing files.

Guidance must fit the requested scope and chosen model. Do not hardcode personal model hierarchies, force project-wide reading for localized changes, repeat already-settled decisions, require unnecessary confirmations or run unrelated suites. Define completion through the required implementation, execution, inspection, correction and validation stages. Preserve intentional approval and production boundaries.

A collection is optional, not a requirement to load every skill. Optional cross-skill references must have a useful fallback. Do not install additional skills merely to satisfy a reference. Report structural validation separately from measured model behavior or performance.
