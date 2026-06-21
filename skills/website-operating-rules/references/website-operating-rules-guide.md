# Website Operating Rules Guide

## Purpose

Make the default website workflow disciplined enough to prevent rushed, generic output.

## Use When

- Any website/app request involving creation, redesign, visual review, UI implementation, polish, or deployment.
- Open-ended prompts such as build a beautiful site, make it modern, make it premium, make it like Squarespace, Raycast, Linear, Vercel, or cinematic references.
- Cases where the user has strong taste expectations but has not yet provided a full brief.

## Do Not Use When

- Backend-only work with no UI surface.
- Tiny copy-only edits where no frontend behavior or design is involved.
- A code review where the user explicitly wants only bugs/security findings.

## Discovery Questions

- What is the site category: business, portfolio, product, luxury/editorial, commerce, dashboard, docs, game, tool?
- What are the existing framework, entry file, styling system, and motion/JS systems?
- What assets exist and which are missing: logo, copy, imagery, video, screenshots, product UI, fonts?
- Did the user clearly say proceed, or should planned files be confirmed before major changes?

## Decision Tree

- If code exists, inspect files and commands before proposing implementation.
- If no code exists, choose a conservative modern stack only after naming why it fits the site.
- If the task is open-ended, create a design direction or blueprint before coding.
- If the site can run locally, run it and visually inspect desktop/mobile before final answer.
- If checks cannot run, state exactly why and what was still inspected.

## Implementation Rules

- Treat visual QA as part of the work, not an optional afterthought.
- Never let generic placeholders survive into final delivery unless the user explicitly accepts placeholders.
- Keep edits scoped to the requested site, but do enough polish to make the changed area feel finished.
- Prefer concrete acceptance criteria over subjective assurances like looks good.
- When references conflict, choose a primary reference family and state which traits are being borrowed.

## Useful Patterns

- Discovery -> plan -> build -> run -> inspect -> polish -> verify -> summarize.
- Use a short design contract for open-ended builds: mood, layout grammar, type, color, media, motion, QA.
- Pair high-level taste skills with implementation skills: style director plus Next/Tailwind/Motion/GSAP as needed.

## Anti-Patterns

- Starting by installing dependencies without reading the repo.
- Shipping a page that compiles but was never viewed.
- Saying premium/cinematic/modern without showing how that changed type, layout, assets, and motion.
- Leaving default buttons, unstyled forms, orphan text, or mobile overflow.

## QA Checklist

- Confirm exact commands run: lint, build, tests, dev server, browser checks.
- Check at least one desktop and one mobile viewport when tooling permits.
- Look for horizontal scroll, text overflow, broken images, console errors, and interaction states.
- Mention missing verification if network, dependencies, credentials, or tooling block checks.

## Acceptance Criteria

- The final work is traceable from brief to files to verification.
- The user can understand what changed and how to view it.
- The visible page has had at least one deliberate polish pass.

## Shared Website Requirements

- Inspect before coding: project structure, framework, homepage/main entry, styling system, interaction/motion system, assets, and available commands.
- Before major changes, explain planned files and wait unless the user clearly says proceed, build, create, implement, fix, continue, or similar.
- Use existing project conventions first; explain major dependencies before adding them.
- Default to premium modern quality without generic SaaS/agency/template patterns.
- Prefer real, generated, or art-directed visuals when the subject benefits from images, video, product UI, or spatial media.
- Build version 1, inspect the rendered result, improve visual quality, then run available checks again.
- Check desktop and mobile. Keep text readable, avoid overlaps, respect focus states and reduced motion.
- Report files changed, commands run, visual checks completed, and anything not tested.
