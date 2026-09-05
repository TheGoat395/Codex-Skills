---
name: animation-tool-router
description: "Resolve motion tools or native View Transitions."
---

# Animation Tool Router

Use this skill when motion-tool choice is unresolved. Retain a capable existing choice; choose the lightest option that satisfies the purpose and constraints.

## Routing

- CSS transitions: hover/focus states, small fades, transforms, simple menus.
- Motion: React component animation, layout transitions, presence, gestures, small scroll reveals.
- GSAP: precise timelines, pinned scroll scenes, split text, SVG paths, complex choreography.
- Lenis: smooth scroll feel when the project can support it and anchor/modal behavior is handled.
- Native browser or supported React View Transitions: continuity when the installed router/runtime and browser floor support them; retain fallback behavior and do not force an experimental upgrade.
- Rive or dotLottie: authored timeline or interactive state-machine assets; choose from the existing asset, runtime support and accessible fallback. Plain Lottie remains useful for compatible exported vector motion.
- Three.js/R3F or shaders: requested spatial, material, generative or atmospheric brand visuals when their purpose and performance budget justify the cost.
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
