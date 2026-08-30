#!/usr/bin/env node
import { createRequire } from 'node:module';
import { createHash } from 'node:crypto';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';

const [url, outputDir] = process.argv.slice(2);
if (!url || !outputDir) { console.error('Usage: capture-settled-baseline.mjs <url> <output-dir>'); process.exit(2); }
const require = createRequire(resolve(process.cwd(), 'package.json'));
const { chromium } = require('@playwright/test');
const directory = resolve(outputDir); await mkdir(directory, { recursive: true });
const browser = await chromium.launch();
const cases = [
  { id: 'desktop', width: 1440, height: 1100, reducedMotion: 'no-preference' },
  { id: 'mobile', width: 390, height: 844, reducedMotion: 'no-preference' },
  { id: 'reduced', width: 1440, height: 1100, reducedMotion: 'reduce' },
];
const records = [];
for (const item of cases) {
  const context = await browser.newContext({ viewport: { width: item.width, height: item.height }, reducedMotion: item.reducedMotion });
  const page = await context.newPage(); const consoleErrors = []; const failedResponses = [];
  page.on('console', message => { if (message.type() === 'error') consoleErrors.push(message.text()); });
  page.on('response', response => { if (response.status() >= 400) failedResponses.push({ status: response.status(), url: response.url() }); });
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.evaluate(async () => { await document.fonts.ready; for (let y = 0; y < document.documentElement.scrollHeight; y += innerHeight * .8) { scrollTo(0, y); await new Promise(r => setTimeout(r, 80)); } scrollTo(0, 0); });
  await page.waitForTimeout(item.reducedMotion === 'reduce' ? 150 : 1300);
  const layout = await page.evaluate(() => ({ overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth, canvases: [...document.querySelectorAll('canvas')].map(canvas => ({ width: canvas.width, height: canvas.height })) }));
  const screenshot = resolve(directory, `${item.id}.png`); await page.screenshot({ path: screenshot, fullPage: true });
  const sha256 = createHash('sha256').update(await readFile(screenshot)).digest('hex');
  records.push({ ...item, screenshot, sha256, consoleErrors, failedResponses, ...layout }); await context.close();
}
await browser.close();
await writeFile(resolve(directory, 'visual-baseline-manifest.json'), JSON.stringify({ url, capturedAt: new Date().toISOString(), records }, null, 2) + '\n');
if (records.some(r => r.overflow || r.consoleErrors.length || r.failedResponses.length)) process.exitCode = 1;
