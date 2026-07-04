# Claude Code Adapter

Claude Code supports `SKILL.md` skill folders. That makes this repo's skill folders directly portable after review.

## Personal Install

Install selected skills for all Claude Code projects:

```bash
mkdir -p ~/.claude/skills
cp -R skills/website-blueprint-first ~/.claude/skills/
cp -R skills/web-style-director ~/.claude/skills/
cp -R skills/anti-generic-website-review ~/.claude/skills/
cp -R skills/responsive-visual-polish-qa ~/.claude/skills/
cp -R skills/browser-inspection-workflow ~/.claude/skills/
cp -R skills/final-client-handoff ~/.claude/skills/
```

## Project Install

Install selected skills for one repository:

```bash
mkdir -p .claude/skills
cp -R skills/website-blueprint-first .claude/skills/
cp -R skills/web-style-director .claude/skills/
cp -R skills/anti-generic-website-review .claude/skills/
cp -R skills/responsive-visual-polish-qa .claude/skills/
cp -R skills/browser-inspection-workflow .claude/skills/
cp -R skills/final-client-handoff .claude/skills/
```

## Recommended Claude Starter Set

Use this small set first:

| Skill | Purpose |
|---|---|
| `website-blueprint-first` | Plan website structure before building. |
| `web-style-director` | Decide visual direction from the brief. |
| `anti-generic-website-review` | Catch generic AI website patterns. |
| `responsive-visual-polish-qa` | Check desktop and mobile polish. |
| `browser-inspection-workflow` | Inspect rendered output. |
| `final-client-handoff` | Summarize delivery and verification. |

## Full Public Core

For a full local copy, use:

```bash
mkdir -p ~/.claude/skills
cp -R skills/* ~/.claude/skills/
```

Review the skills before installing the full public core. A focused starter set is usually easier to evaluate.

## Invocation

Claude Code exposes skills through slash commands based on skill directory names. For example:

```text
/anti-generic-website-review
/browser-inspection-workflow
```

Claude Code can also load relevant skills automatically based on descriptions.

## Notes

- This adapter does not change the skill content.
- Keep the source repo as the reviewed copy.
- Re-copy selected skills after updating the repo.
- This project is unofficial and is not endorsed by Anthropic.
