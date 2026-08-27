import pytest
from playwright.sync_api import Page, expect

def test_app_startup_and_multimind_surface(page: Page):
    page.goto("http://localhost:3000")
    page.wait_for_selector("#app-container", timeout=15000)

    # Check tabs present
    expect(page.locator("#tab-multimind")).to_be_visible()
    expect(page.locator("#tab-ref-a")).to_be_visible()
    expect(page.locator("#tab-ref-b")).to_be_visible()
    expect(page.locator("#tab-ref-c")).to_be_visible()
    expect(page.locator("#tab-ref-d")).to_be_visible()

def test_reference_surfaces_render(page: Page):
    page.goto("http://localhost:3000")
    page.wait_for_selector("#app-container", timeout=15000)

    # Check Ref A
    page.click("#tab-ref-a")
    page.wait_for_selector("#reference-arknights", timeout=5000)
    expect(page.locator("#reference-arknights")).to_be_visible()

    # Check Ref B
    page.click("#tab-ref-b")
    page.wait_for_selector("#reference-noomo", timeout=5000)
    expect(page.locator("#reference-noomo")).to_be_visible()

    # Check Ref C
    page.click("#tab-ref-c")
    page.wait_for_selector("#reference-dioriviera", timeout=5000)
    expect(page.locator("#reference-dioriviera")).to_be_visible()

    # Check Ref D
    page.click("#tab-ref-d")
    page.wait_for_selector("#reference-viensla", timeout=5000)
    expect(page.locator("#reference-viensla")).to_be_visible()

def test_long_conversation_and_live_mutation(page: Page):
    page.goto("http://localhost:3000")
    page.wait_for_selector("#app-container", timeout=15000)
    page.click("#tab-multimind")
    page.wait_for_selector("#morphology-editorial", timeout=5000)

    # Verify Editorial morphology renders
    expect(page.locator("#morphology-editorial")).to_be_visible()

    # Verify 35+ messages rendered
    messages = page.locator("#chat-messages-container > div")
    expect(messages).to_have_count(36)

    # Live Presentation Mutation (Switch morphology without full page refresh)
    page.click("#btn-morphology-switch")
    page.wait_for_selector("#morphology-tactical", timeout=5000)
    expect(page.locator("#morphology-tactical")).to_be_visible()

    # Verify message count preserved
    messages_tactical = page.locator("#chat-messages-container-tactical > div")
    expect(messages_tactical).to_have_count(36)

def test_mobile_view_and_composition(page: Page):
    page.set_viewport_size({"width": 390, "height": 844})
    page.goto("http://localhost:3000")
    page.wait_for_selector("#app-container", timeout=15000)
    page.click("#tab-multimind")

    # Verify layout fits mobile viewport
    expect(page.locator("#tab-multimind")).to_be_visible()
