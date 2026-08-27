import pytest
from playwright.sync_api import Page, expect

def test_app_startup_and_multimind_surface(page: Page):
    page.goto("http://localhost:3000")
    page.wait_for_selector("#app-container", timeout=15000)

    # Check navigation tabs present
    expect(page.locator("#tab-multimind")).to_be_visible()
    expect(page.locator("#tab-ref-a")).to_be_visible()
    expect(page.locator("#tab-ref-b")).to_be_visible()
    expect(page.locator("#tab-ref-c")).to_be_visible()
    expect(page.locator("#tab-ref-d")).to_be_visible()

def test_reference_surfaces_and_interactive_behaviors(page: Page):
    page.goto("http://localhost:3000")
    page.wait_for_selector("#app-container", timeout=15000)

    # 1. Arknights Interactive Deployment Progress
    page.click("#tab-ref-a")
    page.wait_for_selector("#reference-arknights", timeout=5000)
    expect(page.locator("#reference-arknights")).to_be_visible()
    page.click("#btn-arknights-deploy")
    page.wait_for_timeout(500)

    # 2. Noomo Spatial Kinetic Transform
    page.click("#tab-ref-b")
    page.wait_for_selector("#reference-noomo", timeout=5000)
    expect(page.locator("#reference-noomo")).to_be_visible()
    page.click("#btn-noomo-transform")
    page.wait_for_timeout(500)

    # 3. Dioriviera Luxury Full-Bleed Composition
    page.click("#tab-ref-c")
    page.wait_for_selector("#reference-dioriviera", timeout=5000)
    expect(page.locator("#reference-dioriviera")).to_be_visible()

    # 4. Viens-là Layout Mode Toggle
    page.click("#tab-ref-d")
    page.wait_for_selector("#reference-viensla", timeout=5000)
    expect(page.locator("#reference-viensla")).to_be_visible()
    page.click("#btn-viensla-toggle")
    page.wait_for_timeout(500)

def test_long_conversation_zero_reload_and_scroll_preservation(page: Page):
    page.goto("http://localhost:3000")
    page.wait_for_selector("#app-container", timeout=15000)
    page.click("#tab-multimind")
    page.wait_for_selector("#morphology-editorial", timeout=5000)

    # Record page loaded timestamp to verify zero full page reloads
    initial_timestamp = page.evaluate("window.__page_loaded_timestamp")

    # Verify Editorial morphology renders 36 messages
    messages = page.locator("#chat-messages-container > div")
    expect(messages).to_have_count(36)

    # Scroll down chat container
    page.evaluate("document.getElementById('editorial-scroll-area').scrollTop = 400")
    page.wait_for_timeout(300)

    # Trigger Live Presentation Mutation to Tactical Morphology B
    page.click("#btn-morphology-switch")
    page.wait_for_selector("#morphology-tactical", timeout=5000)
    expect(page.locator("#morphology-tactical")).to_be_visible()

    # Verify zero full-page reload
    new_timestamp = page.evaluate("window.__page_loaded_timestamp")
    assert initial_timestamp == new_timestamp, "Full page reload detected during live mutation!"

    # Verify 36 messages preserved
    messages_tactical = page.locator("#chat-messages-container-tactical > div")
    expect(messages_tactical).to_have_count(36)

    # Verify scroll position preserved on Tactical surface
    tactical_scroll = page.evaluate("document.getElementById('tactical-scroll-area').scrollTop")
    assert tactical_scroll >= 300, f"Scroll position not preserved! Expected >=300, got {tactical_scroll}"

def test_mobile_hard_gate_and_purpose_built_surface(page: Page):
    page.set_viewport_size({"width": 390, "height": 844})
    page.goto("http://localhost:3000")
    page.wait_for_selector("#app-container", timeout=15000)
    page.click("#tab-multimind")

    # Assert Mobile Purpose-Built Surface and Controls exist
    expect(page.locator("#mobile-multimind-surface")).to_be_visible()
    expect(page.locator("#btn-mobile-send")).to_be_visible()
    expect(page.locator("#input-mobile-msg")).to_be_visible()

    # Verify mobile style toggle works without destroying session
    page.click("#btn-mobile-toggle")
    page.wait_for_timeout(500)
    expect(page.locator("#mobile-multimind-surface")).to_be_visible()
