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
    # Переход на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Поиск поля ввода (единственное поле на странице)
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Ввод текста "Sky"
    input_field.send_keys("Sky")
    time.sleep(1)

    # Очистка поля
    input_field.clear()
    time.sleep(1)

    # Ввод текста "Pro"
    input_field.send_keys("Pro")
    time.sleep(2)

finally:
    # Закрытие браузера
    driver.quit()