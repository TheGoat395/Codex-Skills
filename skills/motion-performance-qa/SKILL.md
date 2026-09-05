---
name: motion-performance-qa
description: "Review whole motion-system release resilience."
---

# Motion Performance QA

## Use This Skill

Use this skill for release-level coverage across the complete motion system, not for diagnosing one isolated jank symptom.

## Scoped execution

Apply the [shared web contract](../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Required Reference

Read [references/motion-performance-qa-guide.md](references/motion-performance-qa-guide.md) before making architectural or visible UI changes with this skill.

## Scope and evidence

Use for a substantial motion-system review or pre-delivery motion audit. A single measured hitch belongs to `$animation-jank-qa`; preserve resize, route return, cleanup and reduced-motion checks where relevant. Review-only does not implement motion.
