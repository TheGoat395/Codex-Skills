# Agent Adapters

The core repo is built around installable `SKILL.md` folders. Some tools can use those folders directly. Others use project rules or context files. This directory provides compact adapters for those environments.

## Available Adapters

| Adapter | Use When | Path |
|---|---|---|
| Claude Code | You want to use selected `SKILL.md` folders in Claude Code. | `adapters/claude-code/` |
| Cursor | You want project rules that summarize the public core standards. | `adapters/cursor/` |
| Gemini CLI | You want a project context file based on the public core. | `adapters/gemini-cli/` |

## Adapter Philosophy

- Keep the 70-skill public core as the source of truth.
- Use adapters for tools that do not consume the full skill tree directly.
- Keep adapter files compact enough to fit normal project context.
- Prefer clear support levels over inflated compatibility claims.
- Review adapters before copying them into production projects.

## What To Install First

For most users:

1. Start with Codex or Claude Code if you want full `SKILL.md` folder behavior.
2. Use Cursor or Gemini adapters when you want the same standards inside a project that uses rules/context files.
3. Submit issues or PRs when a tool-specific adapter needs better coverage.
