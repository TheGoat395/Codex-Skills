# Quick Start

This guide installs the default public skill collection and gives Codex a practical first task.

## Install

Clone the repository:

```bash
git clone https://github.com/TheGoat395/Codex-Skills.git
cd Codex-Skills
```

Preview the default install:

```bash
python3 scripts/install_skills.py --dry-run
```

Install the default public core:

```bash
python3 scripts/install_skills.py
```

Start a new Codex conversation so skill discovery refreshes.

## First Prompt

Use the installed skills on a real frontend project:

```text
Use the Codex website skills to review my homepage and tell me the highest-impact improvements before launch.
```

## Smaller First Install

Install a focused collection if you want to start with the planning and review workflow:

```bash
python3 scripts/install_skills.py --collection taste-and-build-gates
```

Use `curated_collections.json` or `CURATED_COLLECTIONS.md` to inspect the available collections before installing.
