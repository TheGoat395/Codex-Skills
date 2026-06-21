# Benchmarks

Benchmarks are how this project earns trust. Do not claim that a large skill library is useful because it is large. Show that selected skills improve real workflows.

## Benchmark Format

Each benchmark should include:

- prompt and repo/task context
- selected collection or skills
- baseline run without this skill pack
- skill-assisted run with the same task
- screenshots or screen recordings when frontend output is involved
- build, lint, test, accessibility, or browser QA output
- notes on failures, regressions, and where human judgment still mattered

## Suggested Evaluation Areas

- non-generic website composition
- responsive layout quality
- accessibility and keyboard behavior
- visual hierarchy and typography
- interaction and motion quality
- browser console/network cleanliness
- build and deployment readiness
- quality of handoff summary

## Example Benchmark Template

```md
# Benchmark: Product Site Landing Page

## Task

Build a landing page for [product] in [repo].

## Baseline

- Command/session:
- Skills disabled or not installed:
- Result summary:
- Screenshots:
- Build/test output:

## Skill-Assisted Run

- Collections installed:
- Skills observed:
- Result summary:
- Screenshots:
- Build/test output:

## Comparison

- What improved:
- What did not improve:
- Remaining manual work:
- Reproducibility notes:
```

## Current Status

Benchmarks are planned. Treat the repo as public-ready documentation and packaging work, not as a proven performance claim, until benchmark examples are added.
