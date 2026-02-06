import pytest
from playwright.sync_api import expect

@pytest.mark.only_browser("chromium")
def test_authorized_access(page):
    # При создании страницы Playwright подхватит куки из browser_context_args
    page.goto("https://example.com/protected-page")
    expect(page).to_have_url("https://example.com/protected-page")
    # Дальше можно писать проверки, что пользователь уже авторизован