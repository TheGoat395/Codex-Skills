# Codex Premium Website Skills

An unofficial, open-source Codex skill library for premium frontend, website, and design-engineering workflows.

This repository is prepared around a lean `public-core` collection of 70 skills: design direction, frontend implementation, motion, accessibility, QA, content polish, and maintainer safety.

## What This Is

- A domain-specific Codex skill pack for modern website and app work.
- A curated public core, not a loose dump of every local skill.
- A practical toolkit for React, Next.js, Tailwind, GSAP/Motion, QA, copy, accessibility, source research, and visual polish.
- A repo designed to be inspected, installed selectively, benchmarked, and improved in public.

## What This Is Not

- Not an official OpenAI project.
- Not a guarantee that Codex will produce perfect design or production-ready code without review.
- Not a replacement for project context, real assets, rendered browser inspection, accessibility testing, or engineering judgment.
- Not a reason to install every skill at once. The default install is `public-core`.
- Not a security guarantee. Inspect the repo and installer before running anything.

## Repository Contents

- `skills/` contains individual Codex skill folders.
- `curated_collections.json` defines the default 70-skill public core and smaller installable subcollections.
- `scripts/install_skills.py` installs `public-core` by default or selected collections with `--collection`.
- `THIRD_PARTY_NOTICES.md` records license and notice expectations for the public core.
- `BENCHMARKS.md`, `SKILL_QUALITY_STANDARD.md`, and `SECURITY.md` define how this repo should be evaluated and maintained.
- `manifest.json` and `SKILL_INVENTORY.md` are generated inventory files and should be regenerated before a public release.

## Install

Clone the repo, inspect it, then dry-run the default public core:

```bash
python3 scripts/install_skills.py --dry-run
```

Install the default 70-skill public core:

```bash
python3 scripts/install_skills.py
```

Install a focused collection:

```bash
python3 scripts/install_skills.py --collection motion-core --dry-run
python3 scripts/install_skills.py --collection motion-core
```

List available collections:

```bash
python3 scripts/install_skills.py --list-collections
```

Replace existing skills only after review:

```bash
python3 scripts/install_skills.py --replace
```

The installer skips existing skills by default. When `--replace` is used, existing skill folders are moved into a timestamped backup folder under `~/.codex/skills`.

After installing, start a new Codex conversation so skill discovery refreshes.

## Public Core Collections

- `public-core`: the full 70-skill public release.
- `taste-and-build-gates`: design direction, build gates, anti-generic review, browser inspection, handoff.
- `visual-direction`: references, art direction, typography, color, layout, imagery.
- `frontend-implementation`: React, Next.js, Tailwind, primitives, states, forms, accessibility.
- `qa-production-core`: accessibility, performance, responsive, cross-browser, visual regression, SEO.
- `motion-core`: motion language, React motion, easing, jank prevention, reduced motion, GSAP performance.
- `content-conversion-core`: copy, IA, CTA language, conversion polish, proof.
- `maintainer-safety-core`: checkpoint, undo/revert, install-safety review.

See `CURATED_COLLECTIONS.md` for the full map.

## Quality Bar

Every skill should have:

- a narrow trigger and clear description
- concrete actions rather than vague taste language
- explicit boundaries for when it should not run
- no hidden network, filesystem, or dependency side effects
- project-local dependency guidance
- verification steps when it changes code or frontend output

See `SKILL_QUALITY_STANDARD.md` for contribution criteria.

## Licensing

The root `LICENSE` covers original repository packaging, docs, scripts, and skills that do not carry separate notices. If a skill folder includes a more specific notice, that notice controls for that folder. See `THIRD_PARTY_NOTICES.md`.

## Benchmarking

The goal is not to claim that more skills automatically make better output. The goal is to show measurable workflow improvement. Benchmarks should compare the same task with and without selected skill collections, including screenshots, build logs, accessibility checks, browser QA notes, and final code links.

Use `BENCHMARKS.md` and `examples/README.md` as the reporting template.

## Open Source Positioning

This project is best described as:

> An open-source Codex skill library for premium frontend, website, and design-engineering workflows.

The strongest public contribution is not the size of the library. It is the curation: a lean public core, installable groups, quality standards, safety policy, benchmarks, examples, and real maintenance practices for people building frontend work with Codex.
