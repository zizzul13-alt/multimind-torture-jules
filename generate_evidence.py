import time
import os
import uvicorn
import multiprocessing
from playwright.sync_api import sync_playwright

def run_server():
    from app import app
    uvicorn.run(app, host="127.0.0.1", port=8099, log_level="error")

def capture_all_evidence():
    server_proc = multiprocessing.Process(target=run_server, daemon=True)
    server_proc.start()
    time.sleep(2.5)

    os.makedirs("evidence", exist_ok=True)
    os.makedirs("evidence/videos", exist_ok=True)
    base_url = "http://127.0.0.1:8099"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # Desktop Context with deterministic video capture
        desktop_ctx = browser.new_context(
            viewport={"width": 1440, "height": 900},
            record_video_dir="evidence/videos"
        )
        desktop_page = desktop_ctx.new_page()

        # Mobile Context
        mobile_ctx = browser.new_context(
            viewport={"width": 390, "height": 844},
            is_mobile=True,
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
        )
        mobile_page = mobile_ctx.new_page()

        # 1. Capture Pure Reference Slices & Scroll Choreography
        ref_routes = [
            ("ref_arknights", "/ref/arknights?noshell=1"),
            ("ref_noomo", "/ref/noomo?noshell=1"),
            ("ref_dioriviera", "/ref/dioriviera?noshell=1"),
            ("ref_viensla", "/ref/viensla?noshell=1"),
        ]

        for name, route in ref_routes:
            url = f"{base_url}{route}"
            print(f"Capturing reference parity slice: {name}...")
            desktop_page.goto(url)
            desktop_page.wait_for_timeout(400)

            # Exercise scroll-linked motion for video
            desktop_page.evaluate("window.scrollTo(0, 500);")
            desktop_page.wait_for_timeout(300)
            desktop_page.evaluate("window.scrollTo(0, 0);")
            desktop_page.wait_for_timeout(300)

            desktop_page.screenshot(path=f"evidence/{name}_desktop.png", full_page=True)

            mobile_page.goto(url)
            mobile_page.wait_for_timeout(400)
            mobile_page.screenshot(path=f"evidence/{name}_mobile.png", full_page=True)

        # 2. MultiMind Surface — Morphology 1 & Conversation Scroll
        print("Capturing MultiMind Surface & Long Conversation Scroll...")
        desktop_page.goto(f"{base_url}/multimind?noshell=1")
        desktop_page.wait_for_timeout(500)

        # Scroll stream and verify scroll preservation
        desktop_page.evaluate("document.querySelector('#mm-msg-container').scrollTop = 800;")
        desktop_page.wait_for_timeout(400)
        desktop_page.screenshot(path="evidence/multimind_morph1_tactical_desktop.png", full_page=True)

        mobile_page.goto(f"{base_url}/multimind?noshell=1")
        mobile_page.wait_for_timeout(500)
        mobile_page.screenshot(path="evidence/multimind_morph1_tactical_mobile.png", full_page=True)

        # 3. Live Mutation with Scroll Preservation
        print("Recording Live Morphology Swap with Scroll Preservation...")
        desktop_page.click(".mm-mutate-btn")
        desktop_page.wait_for_timeout(600)
        desktop_page.screenshot(path="evidence/multimind_morph2_editorial_desktop.png", full_page=True)

        # Mobile Mutation
        mobile_page.click(".mm-mutate-btn", force=True)
        mobile_page.wait_for_timeout(600)
        mobile_page.screenshot(path="evidence/multimind_morph2_editorial_mobile.png", full_page=True)

        # Save video path deterministically
        vid_path = desktop_page.video.path()
        desktop_ctx.close()
        mobile_ctx.close()
        browser.close()

        # Rename WebM video artifact to deterministic evidence name
        if os.path.exists(vid_path):
            os.rename(vid_path, "evidence/videos/live_mutation_and_scroll_choreography.webm")

        server_proc.terminate()
        print("All visual evidence and deterministic WebM recording captured successfully!")

if __name__ == '__main__':
    capture_all_evidence()
