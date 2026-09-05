#!/usr/bin/env node
import { createRequire } from 'node:module';
import { createHash } from 'node:crypto';
import { access, mkdir, readFile, writeFile, mkdtemp, copyFile, rm } from 'node:fs/promises';
import { resolve } from 'node:path';

const [url, outputDir] = process.argv.slice(2);
if (!url || !outputDir) { console.error('Usage: capture-settled-baseline.mjs <url> <output-dir>'); process.exit(2); }
const targetUrl = new URL(url);
if (!['http:', 'https:'].includes(targetUrl.protocol)) throw new Error('only http and https URLs are supported');
if (targetUrl.username || targetUrl.password) throw new Error('credential-bearing URLs are not supported');
const require = createRequire(resolve(process.cwd(), 'package.json'));
let chromium;
const resolutionErrors = [];
for (const packageName of ['playwright', '@playwright/test']) {
  try {
    ({ chromium } = require(packageName));
    break;
  } catch (error) {
    resolutionErrors.push(`${packageName}: ${error.message}`);
  }
}
if (!chromium) {
  throw new Error(`Playwright is not resolvable from ${process.cwd()} (${resolutionErrors.join('; ')})`);
}
const directory = resolve(outputDir);
const outputFiles = ['desktop.png', 'mobile.png', 'reduced.png', 'visual-baseline-manifest.json'];
for (const filename of outputFiles) {
  try {
    await access(resolve(directory, filename));
    throw new Error(`refusing to overwrite existing evidence file: ${resolve(directory, filename)}`);
  } catch (error) {
    if (error.code !== 'ENOENT') throw error;
  }
}
await mkdir(directory, { recursive: true });
const staging = await mkdtemp(resolve(directory, ".capture-stage-"));
let browser;
const published = [];
try {
browser = await chromium.launch();
const cases = [
  { id: 'desktop', width: 1440, height: 1100, reducedMotion: 'no-preference' },
  { id: 'mobile', width: 390, height: 844, reducedMotion: 'no-preference' },
  { id: 'reduced', width: 1440, height: 1100, reducedMotion: 'reduce' },
];
const records = [];
for (const item of cases) {
  const context = await browser.newContext({ viewport: { width: item.width, height: item.height }, reducedMotion: item.reducedMotion });
  const page = await context.newPage(); let consoleErrorCount = 0; let failedRequestCount = 0; let pageErrorCount = 0; const failedResponses = [];
  page.on('console', message => { if (message.type() === 'error') consoleErrorCount += 1; });
  page.on('pageerror', () => { pageErrorCount += 1; });
  page.on('requestfailed', () => { failedRequestCount += 1; });
  page.on('response', response => {
    if (response.status() < 400) return;
    const responseUrl = new URL(response.url());
    failedResponses.push({ status: response.status(), url: `${responseUrl.origin}${responseUrl.pathname}` });
  });
  try {
    await page.goto(targetUrl.href, { waitUntil: 'domcontentloaded', timeout: 30000 });
  } catch (error) {
    // Do not attach the raw cause: Playwright navigation errors can contain query credentials.
    throw new Error(`navigation failed (${error?.name || 'Error'}); inspect the target/server separately`);
  }
  let networkIdleTimedOut = false;
  try { await page.waitForLoadState('networkidle', {timeout: 3000}); } catch { networkIdleTimedOut = true; }
  const warm = await page.evaluate(async () => { await Promise.race([document.fonts.ready, new Promise(r => setTimeout(r,3000))]); document.documentElement.style.setProperty('scroll-behavior','auto','important'); const initialHeight=document.documentElement.scrollHeight; if(initialHeight>80000) throw new Error('page exceeds 80000px capture bound'); const stop=Math.min(initialHeight,80000); let steps=0; for (let y=0;y<stop && steps<120;y+=innerHeight*.8,steps++){scrollTo(0,y);await new Promise(r=>setTimeout(r,80));} scrollTo(0,0); return {initialHeight,steps,finalHeight:document.documentElement.scrollHeight}; });
  if(warm.finalHeight>80000 || warm.finalHeight>warm.initialHeight+4) throw new Error('page grew during bounded warmup; use a scoped capture or stabilize content');
  await page.waitForTimeout(item.reducedMotion === 'reduce' ? 150 : 1300);
  const layout = await page.evaluate(() => ({ overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth, canvases: [...document.querySelectorAll('canvas')].map(canvas => ({ width: canvas.width, height: canvas.height })) }));
  const screenshot = resolve(directory, `${item.id}.png`); const stagedScreenshot = resolve(staging, `${item.id}.png`); await page.screenshot({ path: stagedScreenshot, fullPage: true, timeout:30000, animations:"disabled" });
  const sha256 = createHash('sha256').update(await readFile(stagedScreenshot)).digest('hex');
  records.push({ ...item, screenshot, sha256, consoleErrorCount, pageErrorCount, failedRequestCount, failedResponses, networkIdleTimedOut, warm, ...layout }); await context.close();
}
await browser.close(); browser = null;
const recordedUrl = `${targetUrl.origin}${targetUrl.pathname}`;
const manifestPath = resolve(directory, 'visual-baseline-manifest.json');
await writeFile(resolve(staging, "visual-baseline-manifest.json"), JSON.stringify({ url: recordedUrl, capturedAt: new Date().toISOString(), method:"bounded-warmed-full-page", browserEngine:"chromium", viewportEmulation:true, animationsDisabledDuringCapture:true, scrollBehaviorOverridden:true, visualInspectionRequired:true, navigationTimeoutMs:30000, networkIdleTimeoutMs:3000, maxHeight:80000, maxWarmSteps:120, records }, null, 2) + '\n');
const hasIssues = records.some(r => r.overflow || r.consoleErrorCount || r.pageErrorCount || r.failedRequestCount || r.failedResponses.length);
for (const filename of outputFiles) { const dest=resolve(directory,filename); await copyFile(resolve(staging,filename),dest,1); published.push(dest); }
console.log(`${hasIssues ? 'CAPTURED_WITH_ISSUES' : 'CAPTURED_REQUIRES_VISUAL_INSPECTION'}: ${records.length} settled baseline states in ${directory}`);
console.log(`MANIFEST: ${manifestPath}`);
if (hasIssues) process.exitCode = 1;

} catch (error) {
 for (const file of published) await rm(file,{force:true}).catch(()=>{});
 throw error;
} finally {
 if(browser) await browser.close().catch(()=>{});
 await rm(staging,{recursive:true,force:true});
}
