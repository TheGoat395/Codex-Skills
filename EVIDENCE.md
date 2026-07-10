# Evidence

This repository is an unofficial open-source Codex skill library. Its evidence is organized so users and reviewers can distinguish existing output proof from estimated impact and future measured benchmarks.

## Current Evidence Status

| Evidence Area | Status | Where To Inspect |
|---|---|---|
| Public skill core | Complete public core of 70 installable skills. | `skills/`, `curated_collections.json`, `SKILL_INVENTORY.md` |
| Installer safety | Dry-run support, collection selection, default skip behavior, and backup-on-replace behavior. | `scripts/install_skills.py`, `INSTALL.md` |
| Ecosystem compatibility | Codex-native install plus Claude Code, Cursor, and Gemini CLI adapter paths. | `COMPATIBILITY.md`, `adapters/` |
| Proof-of-output gallery | Nine checked-in local frontend demos showing the type of output the workflow is meant to support. | `DEMOS.md`, `examples/premium-website-showcase/` |
| Workflow impact estimate | Category-level estimate of expected improvements and risks based on skill coverage. | `examples/benchmarks/premium-website-workflow-estimate/` |
| Measured benchmark | One completed paired baseline-vs-skill-assisted run with saved outputs, checks, scores, and limitations. | `examples/benchmarks/measured-premium-website-template/runs/2026-07-10-atlas/` |
| Maintainer validation | Skill validation workflow runs through GitHub Actions. | `.github/workflows/validate.yml` |

## Proof-of-Output

The showcase gallery contains local frontend artifacts across finance, space travel, security, SaaS, creative studio, and portfolio examples. These demos are useful because they are inspectable files in the repository, not screenshots alone.

Preview locally:

```text
examples/premium-website-showcase/gallery/index.html
```

The gallery demonstrates the repo's intended workflow: install selected skills, provide a prompt/reference/spec, iterate with rendered inspection, and produce polished local frontend artifacts.

## Workflow Impact Assessment

Based on the current public core, the strongest expected gains are:

- stronger upfront design direction before implementation
- fewer generic AI website patterns
- better responsive, accessibility, and browser QA coverage
- clearer motion/tooling decisions
- more systematic final handoff notes
- safer install and maintainer workflows
- broader reuse through Claude Code, Cursor, and Gemini CLI adapter paths

This is an assessment of expected workflow impact, not a completed controlled benchmark.

## Measured Benchmark Status

The first controlled baseline-vs-skill-assisted benchmark is complete and saved under `examples/benchmarks/measured-premium-website-template/runs/2026-07-10-atlas/`. It uses the same prompt, the same Codex CLI model, the same three-file output constraint, and a shared six-category rubric. It is a repository measurement, not an OpenAI evaluation or endorsement.

The run includes:

- the same prompt for both runs
- saved baseline output
- saved skill-assisted output
- JavaScript syntax and structural/accessibility/content checks
- a score table with category-level notes
- browser QA limitations recorded explicitly
- scoring against `BENCHMARKS.md`

The missing piece is rendered browser inspection: no Playwright/Puppeteer runtime was available in the benchmark environment, so no screenshot or browser-console claim is made.

## What Would Strengthen The Evidence

The next evidence upgrades are:

1. A second benchmark task with rendered desktop/mobile screenshots and browser-console notes.
2. Showcase issues from users with screenshots, links, or local preview notes.
3. Focused pull requests that add benchmark results, improve installer safety, or refine skill boundaries.
4. Release downloads and clone traffic from users who inspect or install the public core.
