import { chromium } from '@playwright/test';

async function capture() {
  const browser = await chromium.launch();

  // Desktop Viewport (1440x900)
  const desktopContext = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const dPage = await desktopContext.newPage();

  await dPage.goto('http://localhost:5173/ref-arknights');
  await dPage.waitForSelector('h1');
  await dPage.screenshot({ path: 'evidence/ref_arknights_desktop.png' });

  await dPage.goto('http://localhost:5173/ref-noomo');
  await dPage.waitForSelector('h1');
  await dPage.screenshot({ path: 'evidence/ref_noomo_desktop.png' });

  await dPage.goto('http://localhost:5173/ref-dioriviera');
  await dPage.waitForSelector('h1');
  await dPage.screenshot({ path: 'evidence/ref_dioriviera_desktop.png' });

  await dPage.goto('http://localhost:5173/ref-viensla');
  await dPage.waitForSelector('.giant-heading');
  await dPage.screenshot({ path: 'evidence/ref_viensla_desktop.png' });

  await dPage.goto('http://localhost:5173/');
  await dPage.waitForSelector('.multimind-app[data-morphology="editorial"]');
  await dPage.screenshot({ path: 'evidence/multimind_editorial_desktop.png' });

  await dPage.locator('.editorial-layout .morph-btn').click();
  await dPage.waitForSelector('.multimind-app[data-morphology="tactical"]');
  await dPage.waitForTimeout(200);
  await dPage.screenshot({ path: 'evidence/multimind_tactical_desktop.png' });

  await desktopContext.close();

  // Mobile Viewport (390x844)
  const mobileContext = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const mPage = await mobileContext.newPage();

  await mPage.goto('http://localhost:5173/ref-arknights');
  await mPage.waitForSelector('h1');
  await mPage.screenshot({ path: 'evidence/ref_arknights_mobile.png' });

  await mPage.goto('http://localhost:5173/ref-noomo');
  await mPage.waitForSelector('h1');
  await mPage.screenshot({ path: 'evidence/ref_noomo_mobile.png' });

  await mPage.goto('http://localhost:5173/ref-dioriviera');
  await mPage.waitForSelector('h1');
  await mPage.screenshot({ path: 'evidence/ref_dioriviera_mobile.png' });

  await mPage.goto('http://localhost:5173/ref-viensla');
  await mPage.waitForSelector('.giant-heading');
  await mPage.screenshot({ path: 'evidence/ref_viensla_mobile.png' });

  await mPage.goto('http://localhost:5173/');
  await mPage.waitForSelector('.multimind-app[data-morphology="editorial"]');
  await mPage.screenshot({ path: 'evidence/multimind_editorial_mobile.png' });

  await mPage.locator('.editorial-layout .morph-btn').click();
  await mPage.waitForSelector('.multimind-app[data-morphology="tactical"]');
  await mPage.waitForTimeout(200);
  await mPage.screenshot({ path: 'evidence/multimind_tactical_mobile.png' });

  await mobileContext.close();
  await browser.close();
  console.log('EVIDENCE SCREENSHOTS REGENERATED WITH STRICT VISIBILITY WAITS');
}

capture().catch(console.error);
