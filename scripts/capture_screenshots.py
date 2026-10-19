"""Capture README screenshots of this single-page simulator.

Opens index.html in headless Chromium, runs the simulation with a fixed random
seed, triggers a scenario, and saves PNGs to docs/screenshots/.
Usage: python scripts/capture_screenshots.py
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "screenshots"
OUT.mkdir(parents=True, exist_ok=True)

SCENARIO = sys.argv[1] if len(sys.argv) > 1 else ""
HELP_JS = sys.argv[2] if len(sys.argv) > 2 else ""
SEED = """Math.random = (function(){let s=20261019;return function(){s=(s*16807)%2147483647;return s/2147483647;};})();"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page.add_init_script(SEED)
    page.goto((ROOT / "index.html").as_uri(), wait_until="networkidle")
    page.wait_for_timeout(800)
    page.screenshot(path=str(OUT / "start.png"))

    page.click("#btnStart")
    page.wait_for_timeout(9000)
    if SCENARIO:
        page.evaluate(SCENARIO)
        page.wait_for_timeout(5000)
    page.screenshot(path=str(OUT / "dashboard.png"))
    page.screenshot(path=str(OUT / "full-page.png"), full_page=True)

    page.click("#btnPause")
    page.click("#btnTheory")
    page.wait_for_timeout(700)
    page.screenshot(path=str(OUT / "theory-panel.png"))
    page.click("#btnTheory")
    page.wait_for_timeout(400)

    if HELP_JS:
        page.evaluate(HELP_JS)
        page.wait_for_timeout(600)
        page.screenshot(path=str(OUT / "concept-help.png"))
    browser.close()

for f in sorted(OUT.glob("*.png")):
    print("wrote", f.relative_to(ROOT), f.stat().st_size // 1024, "KB")
