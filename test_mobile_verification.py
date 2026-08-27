import pytest
import time
import multiprocessing
import uvicorn
from playwright.sync_api import sync_playwright

def run_server():
    from app import app
    uvicorn.run(app, host="127.0.0.1", port=8105, log_level="error")

def test_focused_mobile_browser_verification():
    server_proc = multiprocessing.Process(target=run_server, daemon=True)
    server_proc.start()
    time.sleep(2.0)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            # Mobile viewport 390x844
            context = browser.new_context(
                viewport={"width": 390, "height": 844},
                is_mobile=True,
                user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
            )
            page = context.new_page()

            page.on("framenavigated", lambda frame: setattr(page, "_nav_count", getattr(page, "_nav_count", 0) + 1))
            page._nav_count = 0

            page.goto("http://127.0.0.1:8105/multimind?noshell=1")
            initial_nav_count = page._nav_count

            # 1. Verify desktop tactical sidebar is NOT visible on mobile
            assert not page.locator(".mm-tactical-sidebar").is_visible()

            # 2. Verify mobile tactical status surface IS visible
            assert page.locator(".mm-tactical-mobile-bar").is_visible()
            assert "ACTIVE AGENTS: 3" in page.content()

            # 3. Verify mobile agent matrix drawer opens when toggled
            drawer = page.locator("#mob-tactical-drawer")
            assert not drawer.is_visible()
            page.click(".mob-drawer-toggle")
            page.wait_for_timeout(300)
            assert drawer.is_visible()

            # 4. Close drawer and verify live presentation mutation switches to Editorial on mobile without page reload
            page.click(".drawer-close")
            page.wait_for_timeout(200)
            page.click(".mm-mutate-btn")
            page.wait_for_timeout(600)

            assert "MULTIMIND ATELIER" in page.content()
            assert page.locator(".ed-mobile-top-rail").is_visible()

            # 5. Confirm zero page reload occurred
            assert page._nav_count == initial_nav_count

            browser.close()
    finally:
        server_proc.terminate()

if __name__ == "__main__":
    pytest.main(["-v", "test_mobile_verification.py"])
