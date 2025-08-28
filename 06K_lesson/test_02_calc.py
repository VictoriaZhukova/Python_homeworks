from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера Google Chrome
driver = webdriver.Chrome()

try:
    # Переход на страницу калькулятора
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Явное ожидание поля задержки
    wait = WebDriverWait(driver, 10)
    delay_input = wait.until(EC.presence_of_element_located((By.ID, "delay")))

    # Вводим значение 45 в поле задержки
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажимаем кнопки: 7 + 8 =
    def click_button(value):
        button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{value}']")))
        button.click()

    click_button("7")
    click_button("+")
    click_button("8")
    click_button("=")

    # Ожидаем появления результата "15" на экране (до 50 секунд)
    result_locator = (By.CLASS_NAME, "screen")
    WebDriverWait(driver, 50).until(EC.text_to_be_present_in_element(result_locator, "15"))

    # Проверка результата
    screen_text = driver.find_element(*result_locator).text
    assert screen_text == "15", f"Ожидался результат '15', но получено: {screen_text}"

    print("✅ Тест пройден: результат 15 отображается.")

finally:
    driver.quit()
