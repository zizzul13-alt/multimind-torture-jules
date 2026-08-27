import time
from playwright.sync_api import sync_playwright

def capture_all():
    with sync_playwright() as p:
        browser = p.chromium.launch()

        # Desktop Evidence Capture (1440x900)
        page_desktop = browser.new_page(viewport={"width": 1440, "height": 900})
        page_desktop.goto("http://localhost:3000")
        page_desktop.wait_for_selector("#app-container")
        time.sleep(2)

        # 1. MultiMind Morphology A (Editorial)
        page_desktop.click("#tab-multimind")
        time.sleep(1)
        page_desktop.screenshot(path="evidence/desktop_multimind_morphology_a.png")

        # 2. MultiMind Morphology B (Tactical)
        page_desktop.click("#btn-morphology-switch")
        time.sleep(1)
        page_desktop.screenshot(path="evidence/desktop_multimind_morphology_b.png")

        # 3. Reference A
        page_desktop.click("#tab-ref-a")
        time.sleep(1)
        page_desktop.screenshot(path="evidence/desktop_reference_a_arknights.png")

        # 4. Reference B
        page_desktop.click("#tab-ref-b")
        time.sleep(1)
        page_desktop.screenshot(path="evidence/desktop_reference_b_noomo.png")

        # 5. Reference C
        page_desktop.click("#tab-ref-c")
        time.sleep(1)
        page_desktop.screenshot(path="evidence/desktop_reference_c_dioriviera.png")

        # 6. Reference D
        page_desktop.click("#tab-ref-d")
        time.sleep(1)
        page_desktop.screenshot(path="evidence/desktop_reference_d_viensla.png")

        page_desktop.close()

        # Mobile Evidence Capture (390x844)
        page_mobile = browser.new_page(viewport={"width": 390, "height": 844})
        page_mobile.goto("http://localhost:3000")
        page_mobile.wait_for_selector("#app-container")
        time.sleep(2)

        # 1. Mobile MultiMind
        page_mobile.click("#tab-multimind")
        time.sleep(1)
        page_mobile.screenshot(path="evidence/mobile_multimind.png")

        # 2. Mobile Reference A
        page_mobile.click("#tab-ref-a")
        time.sleep(1)
        page_mobile.screenshot(path="evidence/mobile_reference_a_arknights.png")

        # 3. Mobile Reference B
        page_mobile.click("#tab-ref-b")
        time.sleep(1)
        page_mobile.screenshot(path="evidence/mobile_reference_b_noomo.png")

        # 4. Mobile Reference C
        page_mobile.click("#tab-ref-c")
        time.sleep(1)
        page_mobile.screenshot(path="evidence/mobile_reference_c_dioriviera.png")

        # 5. Mobile Reference D
        page_mobile.click("#tab-ref-d")
        time.sleep(1)
        page_mobile.screenshot(path="evidence/mobile_reference_d_viensla.png")

        page_mobile.close()
        browser.close()
        print("All evidence captured successfully.")

if __name__ == "__main__":
    capture_all()
