import pytest
import time
import multiprocessing
import uvicorn
from playwright.sync_api import sync_playwright

def run_server():
    from app import app
    uvicorn.run(app, host="127.0.0.1", port=8109, log_level="error")

def test_scroll_position_preserved_across_mutation():
    server_proc = multiprocessing.Process(target=run_server, daemon=True)
    server_proc.start()
    time.sleep(2.0)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto("http://127.0.0.1:8109/multimind?noshell=1")
            page.wait_for_timeout(500)

            # Scroll down the long conversation container to position 800
            page.evaluate("document.querySelector('#mm-msg-container').scrollTop = 800;")
            page.wait_for_timeout(300)

            initial_scroll = page.evaluate("document.querySelector('#mm-msg-container').scrollTop")
            assert initial_scroll >= 750

            # Trigger Live Presentation Mutation to Editorial Morphology
            page.click(".mm-mutate-btn")
            page.wait_for_timeout(600)

            # Verify morphology mutated to Editorial
            assert "MULTIMIND ATELIER" in page.content()

            # Verify scroll position was restored on the new morphology stream container
            new_scroll = page.evaluate("document.querySelector('.ed-stream-inner').scrollTop")
            assert new_scroll >= 750

            # Mutate back to Tactical Morphology
            page.click(".ed-mutate-btn")
            page.wait_for_timeout(600)

            # Verify scroll position remains preserved in Tactical view
            returned_scroll = page.evaluate("document.querySelector('#mm-msg-container').scrollTop")
            assert returned_scroll >= 750

            browser.close()
    finally:
        server_proc.terminate()

if __name__ == "__main__":
    pytest.main(["-v", "test_scroll_preservation.py"])
