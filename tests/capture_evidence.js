import { chromium } from '@playwright/test';

async function capture() {
  const browser = await chromium.launch();

  // Desktop Viewport (1440x900)
  const desktopContext = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const dPage = await desktopContext.newPage();

  await dPage.goto('http://localhost:5173/ref-arknights');
  await dPage.screenshot({ path: 'evidence/ref_arknights_desktop.png' });

  await dPage.goto('http://localhost:5173/ref-noomo');
  await dPage.screenshot({ path: 'evidence/ref_noomo_desktop.png' });

  await dPage.goto('http://localhost:5173/ref-dioriviera');
  await dPage.screenshot({ path: 'evidence/ref_dioriviera_desktop.png' });

  await dPage.goto('http://localhost:5173/ref-viensla');
  await dPage.screenshot({ path: 'evidence/ref_viensla_desktop.png' });

  await dPage.goto('http://localhost:5173/');
  await dPage.screenshot({ path: 'evidence/multimind_editorial_desktop.png' });

  await dPage.click('.morph-btn');
  await dPage.waitForTimeout(200);
  await dPage.screenshot({ path: 'evidence/multimind_tactical_desktop.png' });

  await desktopContext.close();

  // Mobile Viewport (390x844)
  const mobileContext = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const mPage = await mobileContext.newPage();

  await mPage.goto('http://localhost:5173/ref-arknights');
  await mPage.screenshot({ path: 'evidence/ref_arknights_mobile.png' });

  await mPage.goto('http://localhost:5173/ref-noomo');
  await mPage.screenshot({ path: 'evidence/ref_noomo_mobile.png' });

  await mPage.goto('http://localhost:5173/ref-dioriviera');
  await mPage.screenshot({ path: 'evidence/ref_dioriviera_mobile.png' });

  await mPage.goto('http://localhost:5173/ref-viensla');
  await mPage.screenshot({ path: 'evidence/ref_viensla_mobile.png' });

  await mPage.goto('http://localhost:5173/');
  await mPage.screenshot({ path: 'evidence/multimind_editorial_mobile.png' });

  await mPage.click('.morph-btn');
  await mPage.waitForTimeout(200);
  await mPage.screenshot({ path: 'evidence/multimind_tactical_mobile.png' });

  await mobileContext.close();
  await browser.close();
  console.log('EVIDENCE SCREENSHOTS CAPTURED SUCCESSFULLY');
}

capture().catch(console.error);
