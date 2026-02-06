import time
from playwright.sync_api import Playwright, sync_playwright
def test_or(page):
    page.goto('https://zimaev.github.io/navbar/')
    nav_bar = page.locator('div#navbarNavDropdown')
    nav_bar.locator("li:has-text('Company')").click(modifiers=["Shift"])
    time.sleep(2)
