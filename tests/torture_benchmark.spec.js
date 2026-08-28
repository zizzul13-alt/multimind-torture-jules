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
  });

  test('Reference Proofs Render (A, B, C, D)', async ({ page }) => {
    await page.goto('http://localhost:5173/ref-arknights');
    await expect(page.locator('h1')).toContainText('TACTICAL OPERATIVE TERMINAL');

    await page.goto('http://localhost:5173/ref-noomo');
    await expect(page.locator('h1')).toContainText('INTERACTIVE');

    await page.goto('http://localhost:5173/ref-dioriviera');
    await expect(page.locator('h1')).toContainText('LUXURY MATERIAL COMPOSITION');

    await page.goto('http://localhost:5173/ref-viensla');
    await expect(page.locator('.giant-heading')).toContainText('STRUCTURAL');
  });

  test('Desktop & Mobile Live Presentation Mutation A -> B -> A with State & Scroll Preservation', async ({ page }) => {
    // Reset backend morphology to editorial first
    await page.request.post('http://localhost:8000/api/session/action', {
      data: { action_type: 'change_morphology', payload: { morphology: 'editorial' } }
    });

    await page.goto('http://localhost:5173/');
    await expect(page.locator('.session-title')).toBeVisible();

    const appEl = page.locator('.multimind-app');
    await expect(appEl).toHaveAttribute('data-morphology', 'editorial');

    // Scroll window/page
    await page.evaluate(() => window.scrollTo(0, 400));
    await page.waitForTimeout(100);

    const initialScroll = await page.evaluate(() => window.scrollY);

    // Mutate to Morphology B (Tactical)
    await page.click('.morph-btn');
    await expect(appEl).toHaveAttribute('data-morphology', 'tactical');
    await page.waitForTimeout(100);

    // Verify state preserved without page reload
    const mutatedScroll = await page.evaluate(() => window.scrollY);
    expect(Math.abs(mutatedScroll - initialScroll)).toBeLessThanOrEqual(100);

    // Mutate back B -> A
    await page.click('.morph-btn');
    await expect(appEl).toHaveAttribute('data-morphology', 'editorial');
    await page.waitForTimeout(100);
    const restoredScroll = await page.evaluate(() => window.scrollY);
    expect(Math.abs(restoredScroll - initialScroll)).toBeLessThanOrEqual(100);
  });
});
