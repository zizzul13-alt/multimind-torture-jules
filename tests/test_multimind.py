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

    # 2. Noomo Actual Scroll-Linked Motion
    page.click("#tab-ref-b")
    page.wait_for_selector("#reference-noomo", timeout=5000)
    expect(page.locator("#reference-noomo")).to_be_visible()

    # Trigger scroll event and assert transform change
    page.evaluate("if (window.__trigger_noomo_scroll) { window.__trigger_noomo_scroll(600); }")
    page.wait_for_timeout(300)
    scrolled_transform = page.evaluate("document.getElementById('noomo-kinetic-canvas').style.transform")
    assert "scale" in scrolled_transform and "rotate" in scrolled_transform, f"Noomo kinetic canvas transform not updated on scroll! Got: '{scrolled_transform}'"

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

def test_desktop_scroll_preservation_and_zero_reload(page: Page):
    page.goto("http://localhost:3000")
    page.wait_for_selector("#app-container", timeout=15000)
    page.click("#tab-multimind")
    page.wait_for_selector("#morphology-editorial", timeout=5000)

    # Record page loaded timestamp to verify zero full page reloads
    initial_timestamp = page.evaluate("window.__page_loaded_timestamp")

    # 1. Scroll Editorial container down
    page.evaluate("document.getElementById('editorial-scroll-area').scrollTop = 400")
    page.wait_for_timeout(300)

    # 2. Mutate to Tactical Morphology B
    page.click("#btn-morphology-switch")
    page.wait_for_selector("#morphology-tactical", timeout=5000)

    # Assert zero page reload & Tactical scroll preservation
    assert initial_timestamp == page.evaluate("window.__page_loaded_timestamp")
    tactical_scroll = page.evaluate("document.getElementById('tactical-scroll-area').scrollTop")
    assert tactical_scroll >= 300, f"Tactical scroll not preserved! Expected >=300, got {tactical_scroll}"

    # 3. Mutate back to Editorial Morphology A
    page.click("#btn-morphology-switch-tactical")
    page.wait_for_selector("#morphology-editorial", timeout=5000)

    # Assert zero page reload & Editorial scroll preservation
    assert initial_timestamp == page.evaluate("window.__page_loaded_timestamp")
    editorial_scroll = page.evaluate("document.getElementById('editorial-scroll-area').scrollTop")
    assert editorial_scroll >= 300, f"Editorial scroll not preserved! Expected >=300, got {editorial_scroll}"

def test_mobile_scroll_preservation_and_zero_reload(page: Page):
    page.set_viewport_size({"width": 390, "height": 844})
    page.goto("http://localhost:3000")
    page.wait_for_selector("#app-container", timeout=15000)
    page.click("#tab-multimind")

    initial_ts = page.evaluate("window.__page_loaded_timestamp")

    # 1. Scroll Mobile Editorial container down
    page.evaluate("document.getElementById('mobile-scroll-area-a').scrollTop = 350")
    page.wait_for_timeout(300)

    # 2. Toggle to Mobile Tactical Surface (Morphology B)
    page.click("#btn-mobile-toggle-a")
    page.wait_for_selector("#mobile-tactical-surface", timeout=5000)

    # Assert zero page reload & Mobile Tactical scroll preservation
    assert initial_ts == page.evaluate("window.__page_loaded_timestamp")
    mobile_b_scroll = page.evaluate("document.getElementById('mobile-scroll-area-b').scrollTop")
    assert mobile_b_scroll >= 300, f"Mobile Tactical scroll not preserved! Expected >=300, got {mobile_b_scroll}"

    # 3. Toggle back to Mobile Editorial Surface (Morphology A)
    page.click("#btn-mobile-toggle-b")
    page.wait_for_selector("#mobile-editorial-surface", timeout=5000)

    # Assert zero page reload & Mobile Editorial scroll preservation
    assert initial_ts == page.evaluate("window.__page_loaded_timestamp")
    mobile_a_scroll = page.evaluate("document.getElementById('mobile-scroll-area-a').scrollTop")
    assert mobile_a_scroll >= 300, f"Mobile Editorial scroll not preserved! Expected >=300, got {mobile_a_scroll}"
