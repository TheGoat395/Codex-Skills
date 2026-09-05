# Stitched full-page capture

## When it is warranted

Use settled viewport stitching when a native browser `fullPage` screenshot:

- is blank, gray, white, or mostly empty;
- contains only a narrow strip of the real layout;
- misses lazy-loaded media or lower sections;
- freezes reveal/scroll animation before visible content settles;
- disagrees materially with a working manual scroll or video;
- duplicates or breaks pinned/fixed scenes.

A native full-page capture remains preferable when it accurately matches the rendered page. Stitching is a recovery method, not a mandatory extra step for every site.

## Capture contract

1. Open the real page URL, not a catalog thumbnail or cover asset.
2. Record viewport, device scale, color scheme, reduced-motion state, URL, and time.
3. Wait for document readiness and fonts; inspect console and failed requests.
4. Warm the page from top to bottom so lazy media and reveal sections mount.
5. Return to the top and capture settled viewport slices at deterministic positions.
6. Crop each slice to the next document position and append them vertically so overlap is not duplicated.
7. Inspect the finished image against representative viewport screenshots and the live scroll.

The bundled script requires Playwright resolvable from the current project or `--module-root`, plus ImageMagick's `magick` executable. It writes the image and a JSON sidecar with dimensions, segments, checksum, console/failed-request counts, and capture settings. It does not install dependencies.

The helper warms the exact final scroll position, repeats the warm pass when lazy content changes page height, verifies the stitched dimensions before replacing the destination, and stages output so an earlier file is not overwritten by a failed capture. It rejects credential-bearing URLs and omits query strings from the manifest; avoid signed or token-bearing URLs because third-party browser errors can still expose them outside the manifest.

Useful options:

```bash
node scripts/capture-stitched-full-page.mjs \
  --url http://127.0.0.1:3000 \
  --output artifacts/home-full.png \
  --viewport 1440x1000 \
  --step 850 \
  --wait 1200 \
  --color-scheme dark \
  --reduced-motion no-preference \
  --module-root /path/to/project
```

Use `--suppress-fixed-after-first` only when a small fixed/sticky overlay would otherwise repeat in every slice. The option hides every fixed or sticky element after the first slice, so it can erase full-viewport scenes, pinned storytelling, canvas layers, or essential navigation. Record its use, inspect the result for blank bands, and preserve an unsuppressed comparison.

## Reject the result when

- blank or repeated bands remain;
- page height changed materially during capture;
- lower content or lazy media is absent;
- sticky/pinned content is duplicated in a misleading way;
- canvas, WebGL, or video frames are blank;
- width or crop composition differs from the live viewport;
- console or request failures explain missing content.

Do not infer quality from dimensions or a checksum. Open the image and inspect it. Preserve native and stitched candidates separately when the difference is diagnostically useful.

Primary inspiration: https://github.com/MengTo/Skills/tree/main/agent-skills/codex/stitched-full-page-capture
