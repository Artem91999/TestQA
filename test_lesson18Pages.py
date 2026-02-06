# project/tests/test_lesson18Pages.py
import allure

@allure.story('Login Feature Нина')
@allure.title('Авторизаиця с корректными учетными данными Нины')

def test_login_success(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.navigate()
    login_page.login('admin', 'admin')
    page.pause()
    dashboard_page.assert_welcome_message("Welcome admin")