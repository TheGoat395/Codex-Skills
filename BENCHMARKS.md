# Benchmarks

Benchmarks keep the project grounded in observable workflow quality. The goal is to compare real outputs, not to rely on skill count as a proxy for usefulness.

## Evidence Types

This repository uses two evidence types:

| Type | Purpose | Contents |
|---|---|---|
| Workflow impact estimate | Sets expectations for where the skills should help. | Skill coverage, expected failure modes, category-level improvement estimates. |
| Measured benchmark | Compares actual baseline and skill-assisted outputs. | Prompt, context, outputs, screenshots or recordings, verification notes, and comparison scores. |

## Measured Benchmark Format

Each measured benchmark should include:

- prompt and repo/task context
- selected collection or skills
- baseline run without this skill pack
- skill-assisted run with the same task
- screenshots or screen recordings when frontend output is involved
- build, lint, test, accessibility, or browser QA output
- notes on failures, regressions, and where human judgment still mattered

## Evaluation Areas

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

## Current Evidence

The repo includes:

- a proof-of-output showcase under `examples/premium-website-showcase/`
- a workflow impact estimate under `examples/benchmarks/`
- benchmark scoring criteria for future measured runs

A measured baseline-vs-skill-assisted benchmark is the next evidence upgrade.
