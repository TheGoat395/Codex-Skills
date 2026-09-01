# Skill Catalog

Codex Premium Website Skills ships a curated `public-core` of 80 skills. The public core is organized as installable collections so users can start small, then add more capability as their workflow needs it.

## Collections

| Collection | Status | Best For |
|---|---|---|
| `public-core` | Stable public core | Full 80-skill install for premium frontend, website, and agent-quality workflows. |
| `taste-and-build-gates` | Stable | Design direction, build gates, anti-generic review, browser inspection, and handoff. |
| `visual-direction` | Stable | References, art direction, typography, color, layout, imagery, and screenshot composition. |
| `frontend-implementation` | Stable | React, Next.js, Tailwind, UI primitives, responsive components, state, forms, and accessibility. |
| `qa-production-core` | Stable | Accessibility, performance, mobile, cross-browser, visual regression, and SEO QA. |
| `motion-core` | Stable | Motion language, React motion, easing, jank prevention, reduced motion, and GSAP performance. |
| `content-conversion-core` | Stable | Non-generic copy, IA, content pruning, voice, CTA language, conversion polish, and proof. |
| `maintainer-safety-core` | Stable | Checkpoints, undo/revert behavior, and install-safety review. |
| `agent-quality-core` | Stable | Evidence-led reasoning, research, debugging, agent architecture, memory provenance, evaluation, and completion verification. |

## Recommended Entry Points

| Need | Recommended Collection |
|---|---|
| I want Codex to stop producing generic websites. | `taste-and-build-gates` |
| I need stronger art direction and visual taste. | `visual-direction` |
| I am implementing React or Next.js UI. | `frontend-implementation` |
| I need launch-readiness checks. | `qa-production-core` |
| I want better animation and interaction quality. | `motion-core` |
| I need sharper landing-page copy and proof. | `content-conversion-core` |
| I want safer code-change workflows. | `maintainer-safety-core` |
| I need more rigorous reasoning, research, and agent verification. | `agent-quality-core` |

## High-Value Skills

| Skill | Why Users Reach For It |
|---|---|
| `website-blueprint-first` | Turns vague website requests into a concrete plan before implementation. |
| `web-design-direction-system` | Frames the reader's job, evidence-bearing composition, and repeatable design guidance before visual implementation. |
| `web-style-director` | Converts the brief into a clear visual direction instead of generic UI language. |
| `anti-generic-website-review` | Finds visible AI-site patterns before they ship. |
| `responsive-visual-polish-qa` | Checks mobile and desktop composition, spacing, overflow, and visual balance. |
| `frontend-quality-auditor` | Gives a launch-oriented review of UI, UX, content, accessibility, performance, and trust signals. |
| `browser-inspection-workflow` | Forces rendered browser inspection instead of trusting code alone. |
| `final-client-handoff` | Produces a clear delivery summary with changed files, commands, checks, and limitations. |
| `premium-visual-reference-library` | Guides reference research and taste calibration before visual work. |
| `modern-site-engineering` | Keeps frontend builds aligned with current React, Next.js, and static-site practice. |
| `design-motion-principles` | Adds motion creation and audit workflows with reduced-motion, context, and jank checks. |
| `motion-performance-qa` | Reviews animation performance, cleanup, scroll behavior, and reduced-motion fallbacks. |
| `non-generic-web-copy` | Removes vague AI marketing language and strengthens page-specific copy. |
| `testimonial-proof-systems` | Structures proof without unsupported testimonials or fake metrics. |
| `code-change-safety-checkpoint` | Preserves rollback options before risky edits. |
| `code-change-undo-revert` | Helps undo or revert changes without destroying user work. |
| `critical-thinking` | Reconstructs material claims and tests their evidence before accepting a conclusion. |
| `logical-thinking` | Selects the right inference structure and prevents conclusions from outrunning their premises. |
| `deep-research` | Runs adaptive, source-backed research with explicit coverage, contradiction, and confidence handling. |
| `systematic-debugging` | Localizes failures with competing hypotheses and regression verification. |
| `agent-evaluation-operations` | Turns agent workflows into measurable, reproducible release gates. |

## Install Examples

Install the full public core:

```bash
python3 scripts/install_skills.py
```

Install a focused collection:

```bash
python3 scripts/install_skills.py --collection taste-and-build-gates
```

Dry-run any install first:

```bash
python3 scripts/install_skills.py --collection motion-core --dry-run
```

List all collections:

```bash
python3 scripts/install_skills.py --list-collections
```

## Complete Inventory

For the generated full inventory, see `SKILL_INVENTORY.md`.

For collection membership, see `CURATED_COLLECTIONS.md` and `curated_collections.json`.
