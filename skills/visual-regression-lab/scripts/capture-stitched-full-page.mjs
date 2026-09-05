#!/usr/bin/env node

import { createHash } from 'node:crypto';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { createRequire } from 'node:module';


function usage() {
  console.log(`Usage:
  node capture-stitched-full-page.mjs --url <http(s)://...> --output <image> [options]

Options:
  --viewport <WxH>             Default: 1440x1000
  --step <px>                  Default: viewport height - 150
  --wait <ms>                  Settle wait per slice. Default: 1200
  --navigation-timeout <ms>    Default: 60000
  --max-height <px>            Refuse taller pages. Default: 80000
  --module-root <directory>    Resolve Playwright from this project root
  --manifest <file.json>       Default: <output>.json
  --color-scheme <value>       light, dark, or no-preference. Default: no-preference
  --reduced-motion <value>     reduce or no-preference. Default: no-preference
  --suppress-fixed-after-first Hide fixed/sticky elements after the first slice
  --force                      Replace an existing output and manifest
`);
}


function parseInteger(value, flag) {
  const parsed = Number(value);
  if (!Number.isInteger(parsed) || parsed <= 0) {
    throw new Error(`${flag} requires a positive integer`);
  }
  return parsed;
}


function parseChoice(value, flag, choices) {
  if (!choices.includes(value)) {
    throw new Error(`${flag} requires one of: ${choices.join(', ')}`);
  }
  return value;
}


function parseArgs(argv) {
  const args = {
    url: '',
    output: '',
    viewport: '1440x1000',
    step: 0,
    wait: 1200,
    navigationTimeout: 60000,
    maxHeight: 80000,
    moduleRoot: process.cwd(),
    manifest: '',
    colorScheme: 'no-preference',
    reducedMotion: 'no-preference',
    suppressFixedAfterFirst: false,
    force: false,
    help: false,
  };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === '--help' || arg === '-h') args.help = true;
    else if (arg === '--url') args.url = argv[++index] || '';
    else if (arg === '--output') args.output = argv[++index] || '';
    else if (arg === '--viewport') args.viewport = argv[++index] || '';
    else if (arg === '--step') args.step = parseInteger(argv[++index], '--step');
    else if (arg === '--wait') args.wait = parseInteger(argv[++index], '--wait');
    else if (arg === '--navigation-timeout') args.navigationTimeout = parseInteger(argv[++index], '--navigation-timeout');
    else if (arg === '--max-height') args.maxHeight = parseInteger(argv[++index], '--max-height');
    else if (arg === '--module-root') args.moduleRoot = argv[++index] || '';
    else if (arg === '--manifest') args.manifest = argv[++index] || '';
    else if (arg === '--color-scheme') args.colorScheme = parseChoice(argv[++index], '--color-scheme', ['light', 'dark', 'no-preference']);
    else if (arg === '--reduced-motion') args.reducedMotion = parseChoice(argv[++index], '--reduced-motion', ['reduce', 'no-preference']);
    else if (arg === '--suppress-fixed-after-first') args.suppressFixedAfterFirst = true;
    else if (arg === '--force') args.force = true;
    else throw new Error(`unknown argument: ${arg}`);
  }

  const viewport = /^(\d+)x(\d+)$/.exec(args.viewport);
  if (!viewport) throw new Error(`invalid --viewport value: ${args.viewport}`);
  args.width = parseInteger(viewport[1], '--viewport width');
  args.height = parseInteger(viewport[2], '--viewport height');
  if (!args.step) args.step = Math.max(1, args.height - 150);
  if (args.step > args.height) throw new Error('--step cannot exceed viewport height');
  if (!args.manifest && args.output) args.manifest = `${args.output}.json`;
  return args;
}


function run(command, commandArgs, capture = false) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, commandArgs, {
      stdio: ['ignore', capture ? 'pipe' : 'ignore', 'pipe'],
    });
    let stdout = '';
    let stderr = '';
    if (capture) child.stdout.on('data', (chunk) => { stdout += chunk; });
    child.stderr.on('data', (chunk) => { stderr += chunk; });
    child.on('error', reject);
    child.on('close', (code) => {
      if (code === 0) resolve(stdout);
      else reject(new Error(`${command} failed with exit ${code}: ${stderr.trim()}`));
    });
  });
}


async function requireImageMagick() {
  try {
    await run('magick', ['-version']);
  } catch {
    throw new Error("ImageMagick's magick executable is required but was not found");
  }
  return 'magick';
}


async function refuseExisting(file, force) {
  try {
    await fs.access(file);
    if (!force) throw new Error(`refusing to overwrite existing file without --force: ${file}`);
  } catch (error) {
    if (error.code !== 'ENOENT') throw error;
  }
}


function safeUrl(value) {
  const parsed = new URL(value);
  if (!['http:', 'https:'].includes(parsed.protocol)) {
    throw new Error('only http and https URLs are supported');
  }
  if (parsed.username || parsed.password) {
    throw new Error('credential-bearing URLs are not supported');
  }
  return parsed;
}


async function documentHeight(page) {
  return page.evaluate(() => Math.max(
    document.documentElement.scrollHeight,
    document.body?.scrollHeight || 0,
  ));
}


async function warmPage(page, viewportHeight, waitMs, maxHeight) {
  let previousHeight = -1;
  for (let pass = 0; pass < 3; pass += 1) {
    const height = await documentHeight(page);
    if (height > maxHeight) {
      throw new Error(`page height ${height}px exceeds --max-height ${maxHeight}px`);
    }
    const maxScroll = Math.max(0, height - viewportHeight);
    const positions = [];
    for (let y = 0; y < maxScroll; y += viewportHeight) positions.push(y);
    positions.push(maxScroll);
    for (const y of [...new Set(positions)]) {
      await page.evaluate((scrollY) => window.scrollTo(0, scrollY), y);
      await page.waitForTimeout(Math.min(400, waitMs));
    }
    const resultingHeight = await documentHeight(page);
    if (resultingHeight === height || resultingHeight === previousHeight) break;
    previousHeight = height;
  }
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(waitMs);
  const finalHeight = await documentHeight(page);
  if (finalHeight > maxHeight) {
    throw new Error(`page height ${finalHeight}px exceeds --max-height ${maxHeight}px`);
  }
  return finalHeight;
}


async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    usage();
    return;
  }
  if (!args.url || !args.output) {
    usage();
    throw new Error('--url and --output are required');
  }

  const targetUrl = safeUrl(args.url);
  const output = path.resolve(args.output);
  const manifestPath = path.resolve(args.manifest);
  if(output===manifestPath) throw new Error("output and manifest must be distinct");
  const outputExtension = path.extname(output).toLowerCase();
  if (!['.png', '.jpg', '.jpeg', '.webp'].includes(outputExtension)) {
    throw new Error('--output must end in .png, .jpg, .jpeg, or .webp');
  }
  await refuseExisting(output, args.force);
  await refuseExisting(manifestPath, args.force);
  await fs.mkdir(path.dirname(output), { recursive: true });
  await fs.mkdir(path.dirname(manifestPath), { recursive: true });

  const requireFromProject = createRequire(path.join(path.resolve(args.moduleRoot), 'package.json'));
  let chromium;
  const resolutionErrors = [];
  for (const packageName of ['playwright', '@playwright/test']) {
    try {
      ({ chromium } = requireFromProject(packageName));
      break;
    } catch (error) {
      resolutionErrors.push(`${packageName}: ${error.message}`);
    }
  }
  if (!chromium) {
    throw new Error(`Playwright is not resolvable from --module-root ${path.resolve(args.moduleRoot)} (${resolutionErrors.join('; ')})`);
  }

  const imageMagick = await requireImageMagick();
  const temporaryRoot = await fs.mkdtemp(path.join(os.tmpdir(), 'codex-stitched-capture-'));
  let browser;
  let consoleErrorCount = 0;
  let failedRequestCount = 0;
  let httpErrorCount = 0;
  let pageErrorCount = 0;
  let networkIdleTimedOut = false;
  let page;

  try {
    browser = await chromium.launch({ headless: true });
    page = await browser.newPage({
      viewport: { width: args.width, height: args.height },
      deviceScaleFactor: 1,
      colorScheme: args.colorScheme,
      reducedMotion: args.reducedMotion,
    });
    page.on('console', (message) => {
      if (message.type() === 'error') consoleErrorCount += 1;
    });
    page.on('pageerror', () => { pageErrorCount += 1; });
    page.on('requestfailed', () => { failedRequestCount += 1; });
    page.on('response', (response) => {
      if (response.status() >= 400) httpErrorCount += 1;
    });

    try {
      await page.goto(targetUrl.href, {
        waitUntil: 'domcontentloaded',
        timeout: args.navigationTimeout,
      });
    } catch (error) {
      throw new Error(`navigation failed (${error?.name || 'Error'}); inspect the target and server state separately`);
    }
    await page.evaluate(async () => {
      if (document.fonts?.ready) await Promise.race([document.fonts.ready,new Promise(r=>setTimeout(r,3000))]);
      document.documentElement.style.setProperty('scroll-behavior', 'auto', 'important');
    });
    try {
      await page.waitForLoadState('networkidle', { timeout: Math.min(8000, args.navigationTimeout) });
    } catch {
      networkIdleTimedOut = true; // Bounded settling continues, with uncertainty recorded.
    }

    const captureHeight = await warmPage(page, args.height, args.wait, args.maxHeight);

    const maxScroll = Math.max(0, captureHeight - args.height);
    const intended = [];
    for (let y = 0; y < maxScroll; y += args.step) intended.push(y);
    intended.push(maxScroll);

    const slices = [];
    let fixedElementsSuppressed = false;
    for (let index = 0; index < intended.length; index += 1) {
      await page.evaluate((scrollY) => window.scrollTo(0, scrollY), intended[index]);
      await page.waitForTimeout(args.wait);
      const actualY = await page.evaluate(() => Math.round(window.scrollY));
      if (slices.some((slice) => slice.y === actualY)) continue;
      if (args.suppressFixedAfterFirst && slices.length > 0 && !fixedElementsSuppressed) {
        await page.evaluate(() => {
          for (const element of document.querySelectorAll('body *')) {
            const position = getComputedStyle(element).position;
            if (position === 'fixed' || position === 'sticky') {
              element.setAttribute('data-codex-stitched-hidden', 'true');
              element.style.setProperty('visibility', 'hidden', 'important');
            }
          }
        });
        fixedElementsSuppressed = true;
        await page.waitForTimeout(args.wait);
      }
      const raw = path.join(temporaryRoot, `raw-${String(slices.length + 1).padStart(3, '0')}.png`);
      await page.screenshot({ path: raw, type: 'png', fullPage: false, animations: 'disabled' });
      slices.push({ y: actualY, raw });
    }

    const finalHeight = await documentHeight(page);
    if (Math.abs(finalHeight - captureHeight) > 4) {
      throw new Error(`page height changed during capture (${captureHeight}px to ${finalHeight}px); rerun after content stabilizes`);
    }

    slices.sort((left, right) => left.y - right.y);
    const segments = [];
    for (let index = 0; index < slices.length; index += 1) {
      const nextY = index + 1 < slices.length ? slices[index + 1].y : captureHeight;
      const segmentHeight = nextY - slices[index].y;
      if (segmentHeight <= 0 || segmentHeight > args.height) {
        throw new Error(`invalid stitched segment height ${segmentHeight}px at y=${slices[index].y}`);
      }
      const segment = path.join(temporaryRoot, `segment-${String(index + 1).padStart(3, '0')}.png`);
      await run(imageMagick, [slices[index].raw, '-crop', `${args.width}x${segmentHeight}+0+0`, '+repage', segment]);
      segments.push(segment);
    }

    const stagedOutput = path.join(temporaryRoot, `stitched-output${outputExtension}`);
    await run(imageMagick, [...segments, '-append', stagedOutput]);
    const dimensions = (await run(imageMagick, ['identify', '-format', '%w %h', stagedOutput], true)).trim().split(/\s+/).map(Number);
    if (dimensions.length !== 2 || dimensions[0] !== args.width || dimensions[1] !== captureHeight) {
      throw new Error(`stitched output dimensions ${dimensions.join('x')} do not match expected ${args.width}x${captureHeight}`);
    }
    const outputBytes = await fs.readFile(stagedOutput);
    const outputStat = await fs.stat(stagedOutput);
    const manifest = {
      schemaVersion: '1.2',
      capturedAt: new Date().toISOString(),
      url: `${targetUrl.origin}${targetUrl.pathname}`,
      method: 'settled-viewport-stitching',
      output,
      outputBytes: outputStat.size,
      sha256: createHash('sha256').update(outputBytes).digest('hex'),
      viewport: { width: args.width, height: args.height, deviceScaleFactor: 1 },
      colorScheme: args.colorScheme,
      reducedMotion: args.reducedMotion,
      animationsDisabledDuringCapture: true,
      browserEngine: "chromium", viewportEmulation: true, scrollBehaviorOverridden: true,
      navigationTimeoutMs: args.navigationTimeout, maxHeight: args.maxHeight, networkIdleTimedOut,
      pageHeight: captureHeight,
      step: args.step,
      waitMs: args.wait,
      segmentCount: segments.length,
      suppressFixedAfterFirst: args.suppressFixedAfterFirst,
      consoleErrorCount,
      pageErrorCount,
      failedRequestCount,
      httpErrorCount,
      visualInspectionRequired: true,
    };
    const stagedManifest = path.join(temporaryRoot, 'capture-manifest.json');
    await fs.writeFile(stagedManifest, `${JSON.stringify(manifest, null, 2)}\n`, 'utf8');
    const destinations = [[stagedOutput,output],[stagedManifest,manifestPath]];
    const backups=[]; const published=[]; let safeToRemoveBackups=false;
    try {
      // Backups live beside each destination so restoration stays on that filesystem.
      for(const [,dest] of destinations){
        try { await fs.access(dest); if(!args.force) throw new Error('output appeared during capture'); const backup=dest+'.backup-'+Date.now()+'-'+Math.random().toString(16).slice(2); await fs.copyFile(dest,backup,1); backups.push([backup,dest]); }
        catch(error){if(error.code!=='ENOENT') throw error;}
      }
      for(const [src,dest] of destinations){ await fs.copyFile(src,dest,args.force?0:1); published.push(dest); }
      safeToRemoveBackups=true;
    } catch(error) {
      for(const dest of published) await fs.rm(dest,{force:true});
      for(const [backup,dest] of backups) await fs.copyFile(backup,dest);
      safeToRemoveBackups=true;
      throw error;
    } finally { if(safeToRemoveBackups) for(const [backup] of backups) await fs.rm(backup,{force:true}); }
    const hasIssues=consoleErrorCount||pageErrorCount||failedRequestCount||httpErrorCount;
    if(hasIssues) process.exitCode=1;
    console.log(`${hasIssues?'CAPTURED_WITH_ISSUES':'CAPTURED_REQUIRES_VISUAL_INSPECTION'}: ${output} (${args.width}x${captureHeight}, ${segments.length} segments)`);
    console.log(`MANIFEST: ${manifestPath}`);
  } finally {
    if (page) await page.close().catch(() => {});
    if (browser) await browser.close().catch(() => {});
    await fs.rm(temporaryRoot, { recursive: true, force: true });
  }
}


main().catch((error) => {
  console.error(`ERROR: ${error.message}`);
  process.exit(1);
});
