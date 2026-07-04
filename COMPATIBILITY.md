# Compatibility

Codex Premium Website Skills is built for Codex first and organized around portable `SKILL.md` folders. The core skill content can be used directly by agents that support Agent Skills-style folders, or adapted into project rules and context files for tools that use a different instruction format.

## Support Matrix

| Tool | Support Level | Recommended Path |
|---|---|---|
| Codex | Native supported | Use `scripts/install_skills.py` to install `public-core` or focused collections. |
| Claude Code | Native-compatible | Copy selected folders from `skills/` into `~/.claude/skills/` or `.claude/skills/`. |
| Cursor | Adapter | Use the curated rule summary in `adapters/cursor/`. |
| Gemini CLI | Adapter | Use the context pack in `adapters/gemini-cli/`. |
| Generic `SKILL.md` agents | Portable with review | Copy selected `skills/<name>/` folders into the agent's expected skill directory. |

## Support Levels

| Level | Meaning |
|---|---|
| Native supported | The repo includes a tested install path for this tool. |
| Native-compatible | The tool understands `SKILL.md` skill folders, but users should install into that tool's own skill directory. |
| Adapter | The tool does not consume this repo's full skill tree directly, so this repo provides a compact rule or context pack. |
| Portable with review | The `SKILL.md` content is reusable, but the user's agent may need its own installer or folder layout. |

## Recommended Starting Points

| User Goal | Start Here |
|---|---|
| Better website output in Codex | `python3 scripts/install_skills.py --collection taste-and-build-gates` |
| Claude Code project skill setup | `adapters/claude-code/README.md` |
| Cursor project rules | `adapters/cursor/codex-premium-website-skills.mdc` |
| Gemini CLI project context | `adapters/gemini-cli/GEMINI.md` |
| Browse the public core | `CATALOG.md` |

## Tool Notes

### Codex

Codex is the primary supported environment. The installer copies selected public skills into `~/.codex/skills`, skips existing skills by default, supports `--dry-run`, and backs up replaced skills when `--replace` is used.

### Claude Code

Claude Code supports skills as `SKILL.md` folders in personal and project skill directories. This repo's skill folders are already structured around that pattern, so users can copy selected folders from `skills/` into Claude Code's skill locations.

See `adapters/claude-code/README.md`.

### Cursor

Cursor uses project rules rather than this repo's full skill-folder loader. The Cursor adapter condenses the public core into a project rule focused on premium frontend direction, non-generic UI, responsive QA, motion discipline, and handoff quality.

See `adapters/cursor/README.md`.

### Gemini CLI

Gemini CLI supports project context files such as `GEMINI.md` and configurable context filenames. The Gemini adapter provides a compact context pack that can be copied into a project or merged with an existing `GEMINI.md`.

See `adapters/gemini-cli/README.md`.

## What This Does Not Claim

- Cursor and Gemini adapters are not full one-to-one installs of all 70 skills.
- Adapter files summarize the repo's standards; they do not replace the complete `skills/` directory.
- Users should inspect any third-party skill or adapter before installing it into an agent environment.
- This project is unofficial and is not endorsed by OpenAI, Anthropic, Cursor, Google, or any other platform vendor.
