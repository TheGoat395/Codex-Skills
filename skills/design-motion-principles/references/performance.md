# Performance

## will-change

`will-change` is a targeted hint, not a guaranteed compositor layer. `auto` is the normal default; `all` is not a useful supported value here. Do not set hints globally. If profiling reveals first-frame preparation cost, apply `will-change: transform, opacity` shortly before the relevant interaction and remove it afterward. Persistent hints and large/many layers can consume memory. Do not use them to hide an unexplained bottleneck.

## Rendering cost

Prefer transform and opacity when they match the design; compositing depends on the browser and element. Background-position/background-size, gradient changes, filter, clip-path and masks can require paint or expensive raster work. For moving gradients, consider a transform/opacity-driven pseudo-element and compare actual traces. CSS custom properties do not bypass the rendering pipeline.

Width/height, offsets, margin/padding and font-size can trigger layout. Measured bounded size animation or layout/FLIP is valid when content flow needs it; scaling text is not an automatic substitute. Batch layout reads before writes and avoid repeated forced layout.

## Budget and checks

Use actual frame work, painted area, layer memory, route lifecycle and target device classes rather than a universal element-count limit. Check interruption, resize, route return, cleanup and reduced-motion states. A few huge filtered layers may cost more than many tiny transform elements. Record source-only advice separately from measured runtime evidence.

Primary technical references: https://web.dev/articles/animations-guide ; https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change
