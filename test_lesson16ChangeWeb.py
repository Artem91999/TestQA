import pytest
from playwright.sync_api import Page, expect


def test_stepik_text(page: Page):
    # Блокируем JavaScript Stepik - он перезаписывает наш HTML!
    page.route("**/api/**", lambda route: route.abort())
    page.route("**/static/frontend-build/**", lambda route: route.abort())

    # Подменяем ГЛАВНУЮ страницу
    page.route("**/lesson/825697/step/2*", lambda route: route.fulfill(
        status=200,
        headers={"content-type": "text/html; charset=utf-8"},
        body="""
        <!DOCTYPE html>
        <html>
        <body>
            <h1>Ниночка, ты моя собачка, ай лав ю</h1>
            <p>Тест прошел успешно!</p>
        </body>
        </html>
        """
    ))

    page.goto('https://stepik.org/lesson/825697/step/2?unit=829211',
              wait_until='domcontentloaded')  # Быстрее!

    expect(page.get_by_text("Ниночка, ты моя собачка")).to_be_visible()
    page.pause()