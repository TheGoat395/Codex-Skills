---
name: motion-performance-qa
description: Run a broad pre-delivery motion-system performance review for websites and apps. Use after substantial Motion, GSAP, Lenis, scroll-scene, transition, carousel, or WebGL work to check lifecycle cleanup, competing systems, layout shift, reduced motion, mobile behavior, and performance budgets. Use animation-jank-qa for one reproducible stutter or hitch.
---

# Motion Performance QA

## Use This Skill

Use this skill for release-level coverage across the complete motion system, not for diagnosing one isolated jank symptom.

## Operating Contract

1. Inspect the existing project before changing code.
2. Identify the motion stack, scroll behavior, component lifecycle, reduced-motion handling, and available verification commands.
3. Keep motion purposeful: clarify sequence, focus, depth, tactility, or product understanding.
4. Follow existing project conventions unless a change clearly improves the result.
5. Run available checks and visually inspect responsive/reduced-motion output when the change affects UI.
6. Record the routes, interactions, devices/viewports, budgets, and lifecycle paths actually covered; do not imply whole-site certification from a sample.

## Required Reference

Read [references/motion-performance-qa-guide.md](references/motion-performance-qa-guide.md) before making architectural or visible UI changes with this skill.
