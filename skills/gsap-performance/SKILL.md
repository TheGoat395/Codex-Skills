---
name: gsap-performance
description: "Diagnose GSAP and ScrollTrigger performance."
license: MIT
---

# GSAP Performance

## When to Use This Skill

Apply when the affected animation uses GSAP or ScrollTrigger. Diagnose measured frame, layout/paint or lifecycle cost. Generic motion diagnosis belongs to `animation-jank-qa`, and a broad release review to `motion-performance-qa`.

**Related skills:** `motion-performance-qa`, `animation-jank-qa`, `animation-tool-router`, and `reduced-motion-design`.

## Prefer Transform and Opacity

Animating **transform** (`x`, `y`, `scaleX`, `scaleY`, `rotation`, `rotationX`, `rotationY`, `skewX`, `skewY`) and **opacity** usually avoids layout and can reduce paint cost; compositor isolation depends on the browser, layer composition and effect. Measure instead of assuming GPU acceleration. Avoid animating layout-heavy properties when a transform can achieve the same effect.

- Prefer: **x**, **y**, **scale**, **rotation**, **opacity**.
- Avoid when possible: **width**, **height**, **top**, **left**, **margin**, **padding** because they trigger layout and can cause jank.

GSAP's **x** and **y** use transforms by default; use them instead of **left**/**top** for movement.

## will-change

Use **will-change** selectively on elements that will animate soon. It hints the browser to prepare for animation work, but overusing it can increase memory pressure.

```css
will-change: transform;
```

Remove or narrow `will-change` when an element no longer needs it.

## Batch Reads and Writes

GSAP batches updates internally. When mixing GSAP with direct DOM reads/writes or layout-dependent code, avoid interleaving reads and writes in a way that causes repeated layout thrashing. Prefer doing all reads first, then all writes, or let GSAP handle the writes in one go.

## Many Elements: Staggers and Lists

- Use **stagger** instead of many separate tweens with manual delays when the animation is the same.
- For long lists, consider virtualization or animating only visible items; avoid creating hundreds of simultaneous tweens if it causes jank.
- Reuse timelines where possible; avoid creating new timelines every frame.

## Frequently Updated Properties

Prefer **gsap.quickTo()** for properties that update often, such as mouse-follower x/y. It reuses a single tween instead of creating new tweens on each update.

```javascript
let xTo = gsap.quickTo("#id", "x", { duration: 0.4, ease: "power3" }),
    yTo = gsap.quickTo("#id", "y", { duration: 0.4, ease: "power3" });

document.querySelector("#container").addEventListener("mousemove", (e) => {
  xTo(e.pageX);
  yTo(e.pageY);
});
```

## ScrollTrigger and Performance

- **pin: true** pins the trigger element during the active range; it is not a GPU-promotion guarantee. Pin only the intended surface and inspect spacing and surrounding layout.
- Numeric **scrub** sets catch-up smoothing (seconds). Animation can continue after scrolling stops; it does not inherently reduce work. Measure total frame cost and responsiveness on relevant devices.
- Call **ScrollTrigger.refresh()** only when layout actually changes, such as after content load. Debounce refresh calls when possible.

## Reduce Simultaneous Work

- Pause or kill off-screen or inactive animations when they are not visible, such as when the user navigates away.
- Avoid animating huge numbers of properties on many elements at once; simplify or sequence if needed.

## Best Practices

- Animate **transform** and **opacity** where possible; use **will-change** only on elements that actually animate.
- Use **stagger** instead of many separate tweens with manual delays when the animation is the same.
- Use **gsap.quickTo()** for frequently updated properties.
- Clean up or kill off-screen animations; call **ScrollTrigger.refresh()** when layout changes, debounced when possible.

## Do Not

- Animate **width**, **height**, **top**, or **left** for movement when **x**, **y**, or **scale** can achieve the same look.
- Set **will-change** or **force3D** on every element just in case; reserve them for elements that actually need them.
- Create hundreds of overlapping tweens or ScrollTriggers without testing on lower-end devices.
- Ignore cleanup; stray tweens and ScrollTriggers keep running and can hurt performance and correctness.

Technical semantics: [GSAP ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/). Verify the installed version for implementation details.
