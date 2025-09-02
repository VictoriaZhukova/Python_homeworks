from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class LoginPage:
    """
    Класс, представляющий страницу логина.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы логина.

        :param driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "loginBtn")

    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в поле логина.

        :param username: Строка с логином
        :return: None
        """
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле пароля.

        :param password: Строка с паролем
        :return: None
        """
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self) -> None:
        """
        Нажимает кнопку "Войти".

        :return: None
        """
        self.driver.find_element(*self.login_button).click()
