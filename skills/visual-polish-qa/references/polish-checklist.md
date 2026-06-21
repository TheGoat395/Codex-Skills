# Visual Polish Checklist

## Viewports

- Desktop around 1440px wide.
- Laptop around 1280px wide.
- Tablet or narrow desktop around 900px wide.
- Mobile around 390px wide.

## Layout

- No unintended horizontal scroll.
- Section rhythm feels deliberate.
- Content width is constrained and readable.
- Repeated elements align cleanly.
- Fixed-format UI has stable dimensions and does not shift on hover/loading.

## Typography

- H1, section headings, labels, body, and captions have distinct roles.
- Long words and labels fit containers.
- Line lengths are comfortable.
- Text does not overlap media or controls.
- Letter spacing is zero unless there is a specific typographic reason.

## Interaction

- Buttons have hover, active, focus-visible, and disabled states when relevant.
- Links are recognizable and keyboard reachable.
- Controls use familiar icons where helpful.
- Motion respects `prefers-reduced-motion`.
- Scroll effects do not trap or hide content.

## Media

- Images and videos load.
- Crops preserve the subject.
- Alt text exists where appropriate.
- Aspect ratios are stable.
- Canvas/WebGL areas are nonblank and correctly framed.

## Build Hygiene

- Run the project's available lint/build/test commands.
- Note any command that cannot run because dependencies, network, credentials, or environment are missing.
- Keep unrelated files untouched.
