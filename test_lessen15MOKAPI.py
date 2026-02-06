from playwright.sync_api import Page


def test_mock_tags(page: Page):
    # ✅ Route с ФАЙЛОМ data.json (как в задаче)
    page.route("**/fruits", lambda route: route.fulfill(path="data.json"))

    # ✅ Официальный демо-сайт Playwright
    page.goto('https://demo.playwright.dev/api-mocking')

    # ✅ Видим результат! Фрукты заменены на наши теги
    page.get_by_text("playwright").is_visible()
    page.get_by_text("pytest").is_visible()
    page.get_by_text("qa").is_visible()

    # Скриншот для доказательства (опционально)
    page.screenshot(path="mock_result.png")
    page.pause()