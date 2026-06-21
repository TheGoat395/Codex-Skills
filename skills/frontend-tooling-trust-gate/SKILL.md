---
name: frontend-tooling-trust-gate
description: "Use before installing or recommending npm packages, GitHub repos, templates, MCP servers, plugins, Codex skills, ChatGPT skills, scripts, CLI tools, design libraries, scraping tools, or AI agent tools for frontend or website work. Produces trust classifications, install-safety decisions, safer alternatives, and project-local/global install guidance."
---

# Frontend Tooling Trust Gate

Use this skill before installing or recommending a repo, package, MCP, plugin, template, or script.

## Trust Classes

- `preferred`: official or clearly reputable.
- `acceptable`: useful, maintained, and reasonably transparent.
- `inspect manually`: promising but insufficiently verified.
- `avoid`: suspicious, stale, unsafe, or low-quality.
- `unknown risk`: not enough evidence.

## Inspection Checklist

1. Prefer official sources, verified orgs, and vendor-maintained repos.
2. Inspect README specificity, license, SECURITY.md, recent commits, releases, issues, and package registry links.
3. Inspect `package.json`, scripts, dependencies, and install instructions.
4. Use `npm view <package> repository license version time maintainers` when npm metadata matters.
5. Look for preinstall/postinstall scripts, broad permissions, telemetry, token requests, cookie access, or curl-to-shell commands.
6. Prefer project-local installs for frontend tools and libraries.
7. Avoid global installs unless the tool is an agent-wide CLI and the user explicitly approves it.
8. Never expose API keys, browser cookies, SSH keys, tokens, or private files to unknown tools.

## Decision Output

Return:

- source and type
- trust class
- evidence
- red flags
- install stance: `install`, `project-local only`, `do not install`, or `needs user auth`
- safer official alternative if rejected
