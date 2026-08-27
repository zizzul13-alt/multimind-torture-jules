import time
import os
import uvicorn
import multiprocessing
from playwright.sync_api import sync_playwright

def run_server():
    from app import app
    uvicorn.run(app, host="127.0.0.1", port=8099, log_level="error")

def capture_all_evidence():
    # Start FastHTML server process
    server_proc = multiprocessing.Process(target=run_server, daemon=True)
    server_proc.start()
    time.sleep(2.5) # Wait for server startup

    os.makedirs("evidence", exist_ok=True)
    base_url = "http://127.0.0.1:8099"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # Desktop context: 1440x900 as mandated by Governor
        desktop_ctx = browser.new_context(viewport={"width": 1440, "height": 900})
        desktop_page = desktop_ctx.new_page()

        # Mobile context: 390x844 as mandated by Governor
        mobile_ctx = browser.new_context(
            viewport={"width": 390, "height": 844},
            is_mobile=True,
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
        )
        mobile_page = mobile_ctx.new_page()

        routes = [
            ("ref_arknights", "/ref/arknights"),
            ("ref_noomo", "/ref/noomo"),
            ("ref_dioriviera", "/ref/dioriviera"),
            ("ref_viensla", "/ref/viensla"),
        ]

        # 1. Capture Reference Proofs (Desktop & Mobile)
        for name, route in routes:
            url = f"{base_url}{route}"
            print(f"Capturing {name}...")
            desktop_page.goto(url)
            desktop_page.wait_for_timeout(500)
            desktop_page.screenshot(path=f"evidence/{name}_desktop.png", full_page=True)

            mobile_page.goto(url)
            mobile_page.wait_for_timeout(500)
            mobile_page.screenshot(path=f"evidence/{name}_mobile.png", full_page=True)

        # 2. Capture MultiMind Surface — Morphology 1 (Tactical) Desktop & Mobile
        print("Capturing MultiMind Morphology 1 (Tactical)...")
        desktop_page.goto(f"{base_url}/multimind")
        desktop_page.wait_for_timeout(500)
        desktop_page.screenshot(path="evidence/multimind_morph1_tactical_desktop.png", full_page=True)

        mobile_page.goto(f"{base_url}/multimind")
        mobile_page.wait_for_timeout(500)
        mobile_page.screenshot(path="evidence/multimind_morph1_tactical_mobile.png", full_page=True)

        # 3. Trigger Live Mutation via HTMX & Capture Morphology 2 (Editorial)
        print("Triggering Live Presentation Mutation via HTMX...")
        desktop_page.click(".mm-mutate-btn")
        desktop_page.wait_for_timeout(600)
        desktop_page.screenshot(path="evidence/multimind_morph2_editorial_desktop.png", full_page=True)

        # Mobile mutation
        mobile_page.click(".mm-mutate-btn")
        mobile_page.wait_for_timeout(600)
        mobile_page.screenshot(path="evidence/multimind_morph2_editorial_mobile.png", full_page=True)

        # 4. Trigger Dynamic Agent Loading State
        print("Triggering Agent Step / Debate State...")
        desktop_page.click(".ed-step-btn")
        desktop_page.wait_for_timeout(500)
        desktop_page.screenshot(path="evidence/multimind_debate_state_updated.png", full_page=True)

        browser.close()
        server_proc.terminate()
        print("All visual evidence captured successfully!")

if __name__ == '__main__':
    capture_all_evidence()
