import pytest
import time
import multiprocessing
import uvicorn
from playwright.sync_api import sync_playwright

def run_server():
    from app import app
    uvicorn.run(app, host="127.0.0.1", port=8101, log_level="error")

def test_live_mutation_and_state_preservation():
    server_proc = multiprocessing.Process(target=run_server, daemon=True)
    server_proc.start()
    time.sleep(2.0)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Track full page navigation reloads
            reloaded = False
            page.on("framenavigated", lambda frame: setattr(page, "_nav_count", getattr(page, "_nav_count", 0) + 1))
            page._nav_count = 0

            page.goto("http://127.0.0.1:8101/multimind")
            assert "TACTICAL OPS SURFACE" in page.content()
            initial_nav_count = page._nav_count

            # Trigger live presentation mutation via HTMX button click
            page.click(".mm-mutate-btn")
            page.wait_for_timeout(500)

            # 1. Verify visual morphology changed live
            assert "MULTIMIND ATELIER" in page.content()
            assert "JOURNAL USER: Dr. Aris Thorne" in page.content()

            # 2. Verify NO full page navigation refresh occurred during mutation
            assert page._nav_count == initial_nav_count

            # 3. Verify state preservation (in-memory long conversation messages intact)
            assert "Dr. Aris Thorne" in page.content()
            assert "FastHTML shifts rendering load entirely to the server" in page.content()

            browser.close()
    finally:
        server_proc.terminate()
