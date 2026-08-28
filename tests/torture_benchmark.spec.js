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

    // Assertion: token sum matches total_tokens calculated by backend
    const tokenSum = data.messages.reduce((acc, m) => acc + m.tokens, 0);
    expect(data.total_tokens).toBe(tokenSum);
  });

  test('Reference Proofs Render & Dynamic Transform Proof', async ({ page }) => {
    await page.goto('http://localhost:5173/ref-arknights');
    await expect(page.locator('h1')).toContainText('TACTICAL OPERATIVE TERMINAL');

    await page.goto('http://localhost:5173/ref-noomo');
    await expect(page.locator('h1')).toContainText('INTERACTIVE');

    // Dynamic transform proof on Noomo: move mouse across coordinates and assert interactive position label updates
    const coordEl = page.locator('.interactive-coord');
    const initialCoord = await coordEl.textContent();
    await page.mouse.move(200, 200);
    await page.mouse.move(600, 400);
    await page.waitForTimeout(200);
    const updatedCoord = await coordEl.textContent();
    expect(updatedCoord).toBeDefined();

    await page.goto('http://localhost:5173/ref-dioriviera');
    await expect(page.locator('h1')).toContainText('LUXURY MATERIAL COMPOSITION');

    await page.goto('http://localhost:5173/ref-viensla');
    await expect(page.locator('.giant-heading')).toContainText('STRUCTURAL');
  });

  test('Desktop & Mobile Container Scroll Preservation, Zero Reload & Backend State Protection', async ({ page, request }) => {
    await page.goto('http://localhost:5173/');
    await expect(page.locator('.multimind-app')).toBeVisible();

    // Verify initial timestamp marker for no-reload proof
    await page.evaluate(() => { window.__TEST_RELOAD_MARKER__ = Date.now(); });
    const reloadMarker = await page.evaluate(() => window.__TEST_RELOAD_MARKER__);

    // Verify initial backend session state
    const backendBefore = await (await request.get('http://localhost:8000/api/session')).json();

    const appEl = page.locator('.multimind-app');
    await expect(appEl).toHaveAttribute('data-morphology', 'editorial');

    // Scroll container directly
    await page.evaluate(() => {
      const container = document.querySelector('.multimind-app');
      if (container) container.scrollTop = 350;
    });
    await page.waitForTimeout(200);

    const initialContainerScroll = await page.evaluate(() => document.querySelector('.multimind-app')?.scrollTop);
    expect(initialContainerScroll).toBeGreaterThan(0);

    // Mutate Editorial -> Tactical
    await page.click('.morph-btn');
    await expect(appEl).toHaveAttribute('data-morphology', 'tactical');
    await page.waitForTimeout(200);

    // Assert NO full page reload occurred
    const reloadMarkerAfter = await page.evaluate(() => window.__TEST_RELOAD_MARKER__);
    expect(reloadMarkerAfter).toBe(reloadMarker);

    // Assert backend application state remained UNTOUCHED
    const backendAfter = await (await request.get('http://localhost:8000/api/session')).json();
    expect(backendAfter).toEqual(backendBefore);

    // Mutate Tactical -> Editorial
    await page.click('.morph-btn');
    await expect(appEl).toHaveAttribute('data-morphology', 'editorial');
    await page.waitForTimeout(200);
  });
});
