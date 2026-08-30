---
name: animation-jank-qa
description: "Diagnose and repair a concrete animation-jank symptom in a rendered website or app. Use for stutter, frame drops, scroll hitching, pinned-scene jumps, parallax lag, input delay, or a reproducible transition problem. Use motion-performance-qa for a broad pre-delivery motion-system review."
---

# Animation Jank QA

Use this skill for symptom-led runtime diagnosis. Start from a reproducible jank case and determine whether it comes from main-thread work, layout/paint, asset pressure, scroll coupling, competing animation systems, or lifecycle cleanup.

## Workflow

1. Reproduce the exact affected route, interaction, viewport, and device class.
2. Read [Animation Jank QA Guide](references/animation-jank-qa-guide.md) before claiming the site is ready.
3. Run the narrowest meaningful trace or rendered check for the symptom; inspect frame timing, long tasks, forced layout, paint/compositing, asset decode, observers, timers, and RAF loops as applicable.
4. Fix issues when they are in scope; otherwise record exact evidence and remaining risk.
5. Retest the original symptom and summarize commands, URLs, traces/screenshots, changed files, and what was not tested.

## Always Protect

- Inspect the framework, motion stack, affected media, component lifecycle, and available browser/performance tooling before changing code.
- Do not claim something was tested unless it was actually tested; report exact commands, URLs, screenshots, viewports, failures, skipped checks, and remaining risk.
- Verify desktop and mobile rendered output, not only source code. For visual or motion work, inspect screenshots, browser behavior, console errors, network failures, and responsive layout.
- Respect accessibility, performance, reduced-motion, and no-JavaScript/no-WebGL/no-autoplay fallbacks where relevant.
- Keep secrets out of code, logs, screenshots, summaries, widgets, and committed files.
- Prefer project-local tooling and existing scripts before adding dependencies. Explain any new dependency before installing it.
- End with a concise handoff: changed files, commands run, checks passed, checks not run, deployment URL if any, and next risks.
