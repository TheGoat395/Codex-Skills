---
name: "web-reference-research"
description: "Analyze selected sources: Viktor or MotionSites."
---

# Web Reference Research

## Purpose

Convert taste references into concrete, verifiable design decisions.

## Required Use

Use this skill when the trigger description applies. Keep the `SKILL.md` lean, then read `references/web-reference-research-guide.md` for concrete rules before planning or editing a meaningful website change.

## Scoped execution

Apply the [shared web contract](../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Detailed Guide

Read `references/web-reference-research-guide.md` when this skill is active for a build, redesign, review, or implementation plan.

For item-level motion references, also read [references/reconstruction-manifest.md](references/reconstruction-manifest.md) and validate the research record with `python3 "<skill-root>/scripts/verify-reference-record.py" <record.json>`.

## Scope and evidence

Resolve source fidelity mode before extraction. Exact authorized/supplied-source work preserves requested details; original work needs an originality delta. Motion-specific phase extraction belongs to `$reference-motion-reconstruction`. Empty unavailable-evidence is legitimate when nothing is missing.

For helper-driven evidence, use the [typed record schema](references/evidence-record-schema.md). The helper validates structure only; use actual inspection/test results for claims.

Resolve `<skill-root>` to this skill folder's actual absolute location; preserve project-local module resolution for Node capture tools.

## Optional specialists

reference-motion-reconstruction is optional. Without it, use the bundled reconstruction-manifest guide to record observed phases, trigger, timing, responsive/reduced-motion behavior and missing evidence; do not invent unseen motion.
