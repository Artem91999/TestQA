import time
import re
import pytest
@pytest.fixture
def my_fixture():
    pass
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").press("CapsLock")
    page.get_by_role("textbox", name="What needs to be done?").fill("С")
    page.get_by_role("textbox", name="What needs to be done?").press("CapsLock")
    page.get_by_role("textbox", name="What needs to be done?").fill("Создать новую задачу в тодос")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").check()
    time.sleep(5)

    # ---------------------
    context.close()
    browser.close()
