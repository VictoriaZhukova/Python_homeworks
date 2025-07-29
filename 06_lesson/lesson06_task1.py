from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("http://uitestingplayground.com/ajax")

    # Явное ожидание: кнопка кликабельна
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ajaxButton"))
    )
    button.click()

    # Явное ожидание: плашка появилась и содержит нужный текст
    success_text_locator = (By.CLASS_NAME, "bg-success")
    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element(
            success_text_locator,
            "Data loaded with AJAX get request."
        )
    )

    # Получаем текст из плашки и выводим
    success_text = driver.find_element(*success_text_locator).text
    print("Текст загружен:", success_text)


finally:
    driver.quit()
    