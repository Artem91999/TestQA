import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def test_run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.locator(".new-todo").click()
    page.locator(".new-todo").fill("Привет, это первый мой урок!")
    page.locator(".new-todo").press("Enter")
    page.locator(".new-todo").fill("Привет, это второй мой урок!")
    page.locator(".new-todo").press("Enter")
    time.sleep(2)
    page.locator(".todo-list li:has-text('Привет, это второй мой урок!') input[type=checkbox]").check()

    time.sleep(2)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as p:
    test_run(p)
