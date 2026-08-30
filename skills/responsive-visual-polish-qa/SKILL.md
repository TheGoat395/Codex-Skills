---
name: "responsive-visual-polish-qa"
description: "Run cross-breakpoint visual QA for websites and apps. Use when layout, typography, media crops, navigation, forms, canvas framing, or interaction composition must remain coherent across desktop, laptop, tablet, and mobile widths. Use visual-polish-qa for general art-direction and finish problems at already accepted breakpoints."
---

# Responsive Visual Polish QA

## Purpose

Make cross-breakpoint behavior the quality gate. This skill owns responsive composition, not every category of frontend polish.

## Required Use

Use this skill when the trigger description applies. Keep the `SKILL.md` lean, then read `references/responsive-visual-polish-qa-guide.md` for concrete rules before planning or editing a meaningful website change.

## Operating Contract

1. Inspect before coding when code exists.
2. Define the representative viewport matrix and the responsive invariants that must hold.
3. Explain planned files before major changes unless the user clearly said to proceed.
4. Inspect and repair transitions between breakpoints, not only one desktop and one mobile screenshot.
5. Report commands run, files changed, and anything not tested.

## Detailed Guide

Read `references/responsive-visual-polish-qa-guide.md` when this skill is active for a build, redesign, review, or implementation plan.
