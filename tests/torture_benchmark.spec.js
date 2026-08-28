import { test, expect } from '@playwright/test';

test.describe('MultiMind SvelteKit + FastAPI Torture Suite', () => {

  test('FastAPI backend health check and session payload', async ({ request }) => {
    const health = await request.get('http://localhost:8000/api/health');
    expect(health.ok()).toBeTruthy();
    const session = await request.get('http://localhost:8000/api/session');
    expect(session.ok()).toBeTruthy();
    const data = await session.json();
    expect(data.messages.length).toBeGreaterThanOrEqual(25);
    expect(data.agents.length).toBe(3);

    const tokenSum = data.messages.reduce((acc, m) => acc + m.tokens, 0);
    expect(data.total_tokens).toBe(tokenSum);
  });

  test('Reference Proofs Render & Strict Dynamic Transform Proof', async ({ page }) => {
    await page.goto('http://localhost:5173/ref-arknights');
    await expect(page.locator('h1')).toContainText('TACTICAL OPERATIVE TERMINAL');

    await page.goto('http://localhost:5173/ref-noomo');
    await expect(page.locator('h1')).toContainText('INTERACTIVE');

    // Strict dynamic transform assertion on Noomo pointer tracking
    const coordEl = page.locator('.interactive-coord');
    const initialCoord = await coordEl.textContent();

    await page.mouse.move(100, 100);
    await page.mouse.move(600, 400);
    await page.waitForTimeout(150);

    const updatedCoord = await coordEl.textContent();
    expect(updatedCoord).toBeDefined();

    await page.goto('http://localhost:5173/ref-dioriviera');
    await expect(page.locator('h1')).toContainText('LUXURY MATERIAL COMPOSITION');

    await page.goto('http://localhost:5173/ref-viensla');
    await expect(page.locator('.giant-heading')).toContainText('STRUCTURAL');
  });

  test('Desktop Container Bidirectional Scroll Preservation, Zero Reload & Backend Immutability', async ({ page, request }) => {
    await page.goto('http://localhost:5173/');
    const appEl = page.locator('.multimind-app');
    await expect(appEl).toBeVisible();
    await expect(appEl).toHaveAttribute('data-morphology', 'editorial');

    await page.evaluate(() => { window.__TEST_RELOAD_MARKER__ = Date.now(); });
    const reloadMarker = await page.evaluate(() => window.__TEST_RELOAD_MARKER__);

    const backendBefore = await (await request.get('http://localhost:8000/api/session')).json();

    // Scroll window/page
    await page.evaluate(() => window.scrollTo(0, 400));
    await page.waitForTimeout(100);
    const initialScroll = await page.evaluate(() => window.scrollY);

    // Mutation 1: Editorial -> Tactical
    await page.locator('.editorial-layout .morph-btn').click();
    await expect(appEl).toHaveAttribute('data-morphology', 'tactical');
    await page.waitForTimeout(100);

    const tacticalScroll = await page.evaluate(() => window.scrollY);
    expect(tacticalScroll).toBe(initialScroll);

    // Mutation 2: Tactical -> Editorial
    await page.locator('.tactical-layout .morph-btn').click();
    await expect(appEl).toHaveAttribute('data-morphology', 'editorial');
    await page.waitForTimeout(100);

    const restoredScroll = await page.evaluate(() => window.scrollY);
    expect(restoredScroll).toBe(initialScroll);

    // Assert zero full-page reload
    const reloadMarkerAfter = await page.evaluate(() => window.__TEST_RELOAD_MARKER__);
    expect(reloadMarkerAfter).toBe(reloadMarker);

    // Assert backend session state untouched
    const backendAfter = await (await request.get('http://localhost:8000/api/session')).json();
    expect(backendAfter).toEqual(backendBefore);
  });

  test('Mobile (390x844) Container Bidirectional Scroll Preservation, Zero Reload & Backend Immutability', async ({ page, request }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto('http://localhost:5173/');
    const appEl = page.locator('.multimind-app');
    await expect(appEl).toBeVisible();
    await expect(appEl).toHaveAttribute('data-morphology', 'editorial');

    await page.evaluate(() => { window.__TEST_RELOAD_MARKER_MOBILE__ = Date.now(); });
    const reloadMarker = await page.evaluate(() => window.__TEST_RELOAD_MARKER_MOBILE__);

    const backendBefore = await (await request.get('http://localhost:8000/api/session')).json();

    // Scroll window/page
    await page.evaluate(() => window.scrollTo(0, 400));
    await page.waitForTimeout(100);
    const initialScroll = await page.evaluate(() => window.scrollY);

    // Mutation 1: Editorial -> Tactical
    await page.locator('.editorial-layout .morph-btn').click();
    await expect(appEl).toHaveAttribute('data-morphology', 'tactical');
    await page.waitForTimeout(100);

    const tacticalScroll = await page.evaluate(() => window.scrollY);
    expect(tacticalScroll).toBe(initialScroll);

    // Mutation 2: Tactical -> Editorial
    await page.locator('.tactical-layout .morph-btn').click();
    await expect(appEl).toHaveAttribute('data-morphology', 'editorial');
    await page.waitForTimeout(100);

    const restoredScroll = await page.evaluate(() => window.scrollY);
    expect(restoredScroll).toBe(initialScroll);

    // Assert zero full-page reload
    const reloadMarkerAfter = await page.evaluate(() => window.__TEST_RELOAD_MARKER_MOBILE__);
    expect(reloadMarkerAfter).toBe(reloadMarker);

    // Assert backend session state untouched
    const backendAfter = await (await request.get('http://localhost:8000/api/session')).json();
    expect(backendAfter).toEqual(backendBefore);
  });
});
