---
name: animation-tool-router
description: "Use when planning or implementing website motion, scroll choreography, microinteractions, page transitions, text reveals, pinned sections, smooth scrolling, Lottie, Three.js/R3F, WebGL, or animation-heavy premium sites. Chooses the lightest appropriate tool and defines reduced-motion fallbacks."
---

# Animation Tool Router

Use this skill to choose motion tools by purpose, not hype.

## Routing

- CSS transitions: hover/focus states, small fades, transforms, simple menus.
- Motion: React component animation, layout transitions, presence, gestures, small scroll reveals.
- GSAP: precise timelines, pinned scroll scenes, split text, SVG paths, complex choreography.
- Lenis: smooth scroll feel when the project can support it and anchor/modal behavior is handled.
- Lottie: exported vector motion when file weight and accessibility are acceptable.
- Three.js/R3F: real 3D product/scene work, not decoration.
- No dependency: static content where motion would distract or harm performance.

## Motion Requirements

Define:

- purpose: reveal, continuity, depth, state, tactility, narrative, or product explanation
- trigger: load, hover, focus, click, route, scroll, drag, or viewport
- duration/easing
- reduced-motion fallback
- cleanup/unmount behavior
- performance risks

## Avoid

- animation because the page is otherwise generic
- scroll hijacking
- motion that hides content
- parallax that causes nausea or jank
- WebGL scenes that are blank on mobile
