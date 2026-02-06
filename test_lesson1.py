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
    todo_item = page.locator('li:has-text("Привет, это первый мой урок!")')
    checkbox_full = todo_item.locator('input[type="checkbox"]')
    checkbox_full.click()

    page.locator(".new-todo").fill("Это пустой кружок")
    page.locator(".new-todo").press("Enter")
    time.sleep(5)
    todo_item = page.locator('li:has-text("Это пустой кружок")')

    # Чекбокс внутри этого элемента
    checkbox = todo_item.locator('input[type="checkbox"]')

    # Проверка, что чекбокс не отмечен
    assert checkbox.is_checked() is False
    # Проверка, что чекбокс отмечен
    assert checkbox_full.is_checked() is True

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as p:
    test_run(p)
