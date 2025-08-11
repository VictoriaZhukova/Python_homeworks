from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from calculator_page import CalculatorPage

def test_calculator_sum():
    # Настройки браузера
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Можно убрать, чтобы видеть тест
    driver = webdriver.Chrome(options=chrome_options)

    try:
        page = CalculatorPage(driver)

        # 1. Открыть страницу
        page.open()

        # 2. Ввести задержку 45 сек
        page.set_delay(45)

        # 3. Нажать 7 + 8 =
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

        # 4. Проверить результат через 45 секунд
        result = page.get_result(timeout=50)
        assert result == "15", f"Ожидалось 15, но получилось {result}"

    finally:
        driver.quit()

if __name__ == "__main__":
    test_calculator_sum()
    print("Тест успешно пройден!")

