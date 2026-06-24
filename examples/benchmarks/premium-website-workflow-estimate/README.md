# Projected Impact Estimate: Premium Website Workflow

This document estimates where Codex Premium Website Skills should improve frontend and website work based on skill coverage, checklist coverage, and common failure modes in AI-assisted website generation.

## Task Type

Create a polished local website, landing page, hero section, or portfolio from a prompt, reference, spec, or rough direction.

## Selected Collections

Recommended collections for this workflow:

- `taste-and-build-gates`
- `visual-direction`
- `frontend-implementation`
- `motion-core`
- `qa-production-core`

Representative skills involved include:

- `anti-generic-website-review`
- `website-blueprint-planner`
- `hero-image-art-direction`
- `editorial-typography-systems`
- `color-material-lighting-direction`
- `modern-site-engineering`
- `responsive-layout-polish`
- `animation-tool-router`
- `animation-jank-qa`
- `accessibility-audit-websites`
- `browser-inspection-workflow`
- `image-video-loading-qa`
- `final-client-handoff`

## Expected Improvement Estimate

| Category | Baseline Risk Without Skills | Expected Skill-Assisted Effect | Confidence |
|---|---|---|---|
| Visual direction | Output may default to generic gradients, cards, centered SaaS sections, weak hierarchy, or mismatched brand mood. | Skills add stronger art direction, typography, material choices, layout hierarchy, and anti-generic review. | High |
| Content quality | Copy may be vague, repetitive, overlong, or unsupported by the page structure. | Skills improve information architecture, CTA specificity, content pruning, and brand-aligned interface copy. | Medium-High |
| Frontend implementation | Output may be visually plausible but brittle, poorly organized, or weak on responsive states. | Skills improve component craft, responsive polish, project-local dependency discipline, and maintainable frontend structure. | Medium-High |
| Motion and interaction | Motion may be decorative, excessive, janky, or missing reduced-motion thinking. | Motion routing and jank QA improve animation intent, tool choice, hover/focus states, and reduced-motion fallbacks. | Medium |
| Accessibility | AI-generated sites often miss heading structure, focus states, labels, contrast, keyboard behavior, or reduced-motion preferences. | Accessibility and performance polish skills add explicit review points before final handoff. | Medium-High |
| QA and handoff | Work may be delivered without browser inspection, console/network checks, responsive QA, or clear known limitations. | Browser inspection, image/video loading QA, final handoff, and rollback skills make verification and delivery more systematic. | High |

## Projected Score Movement

Planning estimate using the rubric in `BENCHMARKS.md`:

| Category | Typical Unassisted Risk Score | Projected Skill-Assisted Score | Expected Lift |
|---|---:|---:|---:|
| Visual direction | 2-3 / 5 | 4 / 5 | +1 to +2 |
| Content quality | 2-3 / 5 | 3-4 / 5 | +1 |
| Frontend implementation | 3 / 5 | 4 / 5 | +1 |
| Motion and interaction | 2-3 / 5 | 3-4 / 5 | +1 |
| Accessibility | 2-3 / 5 | 3-4 / 5 | +1 |
| QA and handoff | 1-2 / 5 | 4 / 5 | +2 to +3 |

## Rationale

The strongest expected gains come from adding disciplined workflow stages around the generation process:

1. define taste and direction before building
2. plan content and layout before styling
3. reject generic AI website patterns
4. choose frontend and motion tools deliberately
5. inspect rendered output instead of trusting code alone
6. document verification, limitations, and handoff notes

Those stages target common failure points in AI-assisted frontend work.

## Benchmark Upgrade Path

Convert this estimate into a measured benchmark by running the same task twice: once without the skills and once with the selected collections installed.

## Recommended First Measured Benchmark

Use the same prompt for both runs:

```text
Build a premium landing page for a fictional AI design studio. It should feel editorial, cinematic, responsive, accessible, and non-generic. Include a hero, service section, proof section, selected work, contact CTA, and final handoff notes.
```

Baseline run:

- no Codex skills installed or skills disabled
- save output, screenshots, command logs, and notes

Skill-assisted run:

- install `taste-and-build-gates`, `visual-direction`, `frontend-implementation`, `motion-core`, and `qa-production-core`
- use the same prompt and comparable time budget
- save output, screenshots, command logs, and notes

Compare with the rubric in `BENCHMARKS.md`.
