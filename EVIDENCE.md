# Evidence

This repository is an unofficial open-source Codex skill library. Its evidence is organized so users and reviewers can distinguish existing output proof from estimated impact and future measured benchmarks.

## Current Evidence Status

| Evidence Area | Status | Where To Inspect |
|---|---|---|
| Public skill core | Complete public core of 80 installable skills, including the `agent-quality-core` collection. | `skills/`, `curated_collections.json`, `SKILL_INVENTORY.md` |
| Installer safety | Dry-run support, collection selection, default skip behavior, and backup-on-replace behavior. | `scripts/install_skills.py`, `INSTALL.md` |
| Ecosystem compatibility | Codex-native install plus Claude Code, Cursor, and Gemini CLI adapter paths. | `COMPATIBILITY.md`, `adapters/` |
| Proof-of-output gallery | Nine checked-in local frontend demos showing the type of output the workflow is meant to support. | `DEMOS.md`, `examples/premium-website-showcase/` |
| Workflow impact estimate | Category-level estimate of expected improvements and risks based on skill coverage. | `examples/benchmarks/premium-website-workflow-estimate/` |
| Measured benchmarks | Two completed paired runs with fixed prompts, saved outputs, checks, scores, limitations, and rendered evidence in the second run. | `examples/benchmarks/measured-premium-website-template/runs/` |
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
- more disciplined reasoning, research, debugging, and agent verification workflows
- broader reuse through Claude Code, Cursor, and Gemini CLI adapter paths

This is an assessment of expected workflow impact, not a completed controlled benchmark.

## Measured Benchmark Status

Two controlled baseline-vs-skill-assisted benchmarks are complete. Atlas records source and structural evidence; Signal / Matter adds rendered desktop/mobile screenshots and automated Chromium checks. Both use the same prompt, model, output constraint, and shared six-category rubric within each pair. They are repository measurements, not OpenAI evaluations or endorsements.

The run includes:

- the same prompt for both runs
- saved baseline output
- saved skill-assisted output
- JavaScript syntax and structural/accessibility/content checks
- a score table with category-level notes
- rendered browser QA in the Signal / Matter run, with limitations recorded explicitly
- scoring against `BENCHMARKS.md`

Signal / Matter improved from 23/30 to 28/30 on the repository rubric. The run includes four final screenshots, raw browser results, no-overflow checks at four widths, canvas-pixel checks, mobile menu and Escape checks, motion-state checks, and reduced-motion checks.

## What Would Strengthen The Evidence

The next evidence upgrades are:

1. Showcase issues from users with screenshots, links, or local preview notes.
2. An independently submitted benchmark or focused improvement pull request.
3. Safari and Firefox coverage for a future rendered benchmark.
4. Release downloads and clone traffic from users who inspect or install the public core.
