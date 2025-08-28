from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

# Настройка Firefox
options = Options()
options.add_argument("--width=1200")
options.add_argument("--height=800")

# Инициализация драйвера Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

try:
    # Переход на страницу логина
    driver.get("http://the-internet.herokuapp.com/login")

    # Ввод логина
    driver.find_element(By.ID, "username").send_keys("tomsmith")

    # Ввод пароля
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # Клик по кнопке Login
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    time.sleep(1)  # небольшая пауза, чтобы страница успела обновиться

    # Поиск плашки с сообщением об успехе и вывод её текста
    success_message = driver.find_element(By.ID, "flash").text
    print("Успешный вход:", success_message.strip())

finally:
    # Закрытие браузера
    driver.quit()
