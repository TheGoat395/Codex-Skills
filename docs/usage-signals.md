# Usage Signals

This document explains which public actions help future users and reviewers understand whether the project is useful.

## Most Useful Public Signals

| Signal | Why It Matters |
|---|---|
| Clone the repository | Shows direct interest in inspecting or installing the project. |
| Download the latest release | Shows interest in the packaged public release artifact. |
| Open a Showcase issue | Adds visible proof that the skills were used on a real workflow. |
| Open a Skill Request issue | Shows demand for a specific capability or workflow gap. |
| Open a Bug Report issue | Helps improve installer, docs, safety, or skill behavior. |
| Submit a benchmark PR | Adds controlled evidence of value. |
| Submit a focused improvement PR | Shows community contribution beyond passive interest. |

## Clone-Based Install

```bash
git clone https://github.com/TheGoat395/Codex-Skills.git
cd Codex-Skills
python3 scripts/install_skills.py --dry-run
python3 scripts/install_skills.py
```

## Release-Based Install

Download the latest release archive:

```text
https://github.com/TheGoat395/Codex-Skills/releases/latest
```

Extract it, then run:

```bash
python3 scripts/install_skills.py --dry-run
python3 scripts/install_skills.py
```

## Showcase Submission

Use the Showcase issue template when a workflow produces a useful result. Include:

- project type
- skills or collections used
- what changed
- screenshots, links, or local preview notes
- any limitations or follow-up work

## Benchmark Submission

For stronger evidence, submit a benchmark using `examples/benchmarks/measured-premium-website-template/`.

Useful benchmark submissions include:

- same prompt for baseline and skill-assisted runs
- saved baseline output
- saved skill-assisted output
- screenshots or recordings
- build/lint/test/browser QA notes
- scoring table from `BENCHMARKS.md`
- honest limitations
