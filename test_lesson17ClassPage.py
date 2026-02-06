# project/tests/test_lesson17ClassPage.py
from pages.login_page import LoginPage


def test_login_failure(page):
    login_page = LoginPage(page)
    login_page.navigate()
    page.pause()
    login_page.login('invalid_user', 'invalid_password')
    page.pause()
    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'

