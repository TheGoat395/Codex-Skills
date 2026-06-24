# Benchmarks

Benchmarks keep the project grounded in observable workflow quality. The goal is to compare real outputs, not to rely on skill count as a proxy for usefulness.

## Evidence Types

This repository uses two benchmark evidence types:

1. **Projected impact estimate** — a structured forecast based on skill coverage, checklist coverage, and common workflow failure modes.
2. **Measured benchmark** — a completed baseline-vs-skill-assisted run with saved prompt, task context, outputs, screenshots or screen recordings, and verification notes.

Projected estimates are useful planning documents. Measured benchmarks are the stronger evidence format and should be added as reproducible examples over time.

## Benchmark Format

Each measured benchmark should include:

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

## Scoring Rubric

Use a 1-5 score for each category:

| Score | Meaning |
|---|---|
| 1 | Poor: generic, broken, missing, or risky. |
| 2 | Weak: partially present but needs major manual repair. |
| 3 | Acceptable: usable but still noticeably average or incomplete. |
| 4 | Strong: polished, coherent, and mostly ready after review. |
| 5 | Excellent: professional, distinctive, accessible, responsive, and handoff-ready. |

Recommended categories:

| Category | What to judge |
|---|---|
| Visual direction | Brand fit, originality, composition, material/light quality. |
| Content quality | Specificity, clarity, information architecture, CTA quality, removal of filler. |
| Frontend implementation | Semantic structure, component organization, responsive behavior, maintainability. |
| Motion and interaction | Purposeful motion, hover/focus states, reduced-motion thinking, absence of jank. |
| Accessibility | Keyboard behavior, focus visibility, headings, labels, contrast, reduced-motion support. |
| QA and handoff | Browser inspection, console/network checks, commands run, known limitations, delivery notes. |

## Projected Impact Estimate Template

Use this format before a measured run exists.

```md
# Projected Impact Estimate: [Task Name]

## Task
[Describe the frontend or website task.]

## Selected Skills / Collections
[List skills or collections expected to help.]

## Expected Improvement Areas
| Category | Baseline Risk Without Skills | Expected Skill-Assisted Effect | Confidence |
|---|---|---|---|
| Visual direction |  |  | Low/Medium/High |
| Content quality |  |  | Low/Medium/High |
| Frontend implementation |  |  | Low/Medium/High |
| Motion and interaction |  |  | Low/Medium/High |
| Accessibility |  |  | Low/Medium/High |
| QA and handoff |  |  | Low/Medium/High |

## Benchmark Upgrade Path
Convert this estimate into a measured benchmark by running the same task with and without the selected skills and saving the outputs.
```

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

The repo includes a proof-of-output showcase under `examples/premium-website-showcase/` and a projected benchmark estimate under `examples/benchmarks/`. A measured baseline-vs-skill-assisted benchmark is the next evidence upgrade.