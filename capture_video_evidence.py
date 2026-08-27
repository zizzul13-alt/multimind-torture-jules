import time
from playwright.sync_api import sync_playwright

def record_video():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            record_video_dir="evidence/"
        )
        page = context.new_page()
        page.goto("http://localhost:3000")
        page.wait_for_selector("#app-container")
        time.sleep(1)

        # Scroll long conversation
        page.hover("#editorial-scroll-area")
        page.mouse.wheel(0, 800)
        time.sleep(1)

        # Live presentation mutation
        page.click("#btn-morphology-switch")
        time.sleep(1)

        page.hover("#tactical-scroll-area")
        page.mouse.wheel(0, -400)
        time.sleep(1)

        context.close()

        # Rename output video file to deterministic name
        import os
        for f in os.listdir("evidence"):
            if f.endswith(".webm") and f != "live_mutation_and_scroll_choreography.webm":
                os.rename(os.path.join("evidence", f), "evidence/live_mutation_and_scroll_choreography.webm")
                break
        print("Video evidence recorded successfully.")

if __name__ == "__main__":
    record_video()
