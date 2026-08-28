import { chromium } from '@playwright/test';

async function measure() {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  let jsBytes = 0;
  let cssBytes = 0;
  let totalBytes = 0;
  let requestCount = 0;
  let jsChunks = 0;

  page.on('response', async (response) => {
    requestCount++;
    const url = response.url();
    let size = 0;
    try {
      const buffer = await response.buffer();
      size = buffer.length;
    } catch (e) {
      size = parseInt(response.headers()['content-length'] || '0', 10);
    }
    totalBytes += size;

    if (url.endsWith('.js') || url.includes('/_app/immutable/')) {
      jsBytes += size;
      if (url.endsWith('.js')) jsChunks++;
    } else if (url.endsWith('.css') || response.headers()['content-type']?.includes('css')) {
      cssBytes += size;
    }
  });

  await page.goto('http://localhost:5173/', { waitUntil: 'networkidle' });
  const domNodeCount = await page.evaluate(() => document.querySelectorAll('*').length);

  console.log('--- REPRODUCIBLE MEASURED METRICS ---');
  console.log(`INITIAL_JS_TRANSFER: ${(jsBytes / 1024).toFixed(2)} KB`);
  console.log(`INITIAL_CSS_TRANSFER: ${(cssBytes / 1024).toFixed(2)} KB`);
  console.log(`INITIAL_TOTAL_TRANSFER: ${(totalBytes / 1024).toFixed(2)} KB`);
  console.log(`INITIAL_REQUEST_COUNT: ${requestCount}`);
  console.log(`INITIAL_JS_CHUNKS: ${jsChunks}`);
  console.log(`INITIAL_DOM_NODE_COUNT: ${domNodeCount}`);

  await browser.close();
}

measure().catch(console.error);
