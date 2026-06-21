# Visual Assets Direction Guide

## Purpose

Ensure the site has credible visual material and that assets are framed, optimized, and purposeful.

## Use When

- The site is visual-first: luxury, hospitality, fashion, restaurant, real estate, portfolio, creator, service, product, or commerce.
- A hero or gallery needs imagery/video/generative assets.
- The site currently relies on gradients, blobs, placeholders, or weak stock-like media.

## Do Not Use When

- The site is intentionally text-only and the concept supports it.
- The user forbids image generation/search and no assets are available.

## Discovery Questions

- What is the subject viewers need to inspect: product, person, place, UI, material, outcome?
- What assets exist and what must be generated, searched, mocked, or deferred?
- What aspect ratios are needed for hero, gallery, cards, mobile crops, social previews?
- What alt text and loading behavior are appropriate?

## Decision Tree

- If subject is physical/human/place, use photography or generated bitmap imagery.
- If subject is software, use real/plausible UI screenshots, workflows, code, or interface scenes.
- If subject is abstract service, use practitioner/workspace/process imagery or typographic proof.
- If assets are missing, define temporary asset slots and ask/produce what is needed.

## Implementation Rules

- Every visual asset needs purpose: establish subject, prove capability, set atmosphere, show detail, or guide action.
- Avoid dark blurry backgrounds when inspection matters.
- Define crop/focal point for desktop and mobile.
- Use stable aspect ratios to prevent layout shift.
- Optimize large assets and avoid unnecessary autoplay video.

## Useful Patterns

- Luxury hero: one strong scene plus concise captioning.
- Product hero: screenshot or render with meaningful UI state.
- Portfolio: curated artifact plates and varied crop rhythm.
- Restaurant/hospitality: atmosphere plus concrete menu/location/booking proof.

## Anti-Patterns

- Gradient blobs in place of the actual subject.
- Generic laptop mockups for every software product.
- Stock photos with no relation to the business.
- Images that crop away faces, products, rooms, or UI details on mobile.

## QA Checklist

- Check image/video loading and console/network errors.
- Inspect mobile crops for subject preservation.
- Verify alt text or decorative treatment.
- Confirm media does not obscure text or controls.

## Acceptance Criteria

- The page feels materially real rather than placeholder-driven.
- Visual assets clarify the site rather than merely decorate it.

## Shared Website Requirements

- Inspect before coding: project structure, framework, homepage/main entry, styling system, interaction/motion system, assets, and available commands.
- Before major changes, explain planned files and wait unless the user clearly says proceed, build, create, implement, fix, continue, or similar.
- Use existing project conventions first; explain major dependencies before adding them.
- Default to premium modern quality without generic SaaS/agency/template patterns.
- Prefer real, generated, or art-directed visuals when the subject benefits from images, video, product UI, or spatial media.
- Build version 1, inspect the rendered result, improve visual quality, then run available checks again.
- Check desktop and mobile. Keep text readable, avoid overlaps, respect focus states and reduced motion.
- Report files changed, commands run, visual checks completed, and anything not tested.
