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

The description should explain when the skill should trigger. It should be specific enough that Codex can choose it without guessing.

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
