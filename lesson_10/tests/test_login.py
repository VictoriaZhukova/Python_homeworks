import allure
from lesson_10.pages.login_page import LoginPage

@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Успешная авторизация")
@allure.description("Проверка, что пользователь может успешно войти в систему с корректными данными")
def test_successful_login(driver):
    """
    Тест проверяет успешный вход пользователя на сайт
    """
    login_page = LoginPage(driver)

    with allure.step("Вводим имя пользователя"):
        login_page.enter_username("testuser")

    with allure.step("Вводим пароль"):
        login_page.enter_password("password123")

    with allure.step("Нажимаем кнопку 'Войти'"):
        login_page.click_login()

    with allure.step("Проверяем, что произошёл успешный вход"):
        assert "Dashboard" in driver.title
