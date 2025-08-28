from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка Firefox
options = Options()
options.add_argument("--headless")  # Убери, если хочешь видеть браузер
driver = webdriver.Firefox(options=options)

wait = WebDriverWait(driver, 10)

try:
    # 1. Открываем сайт
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизация
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавление товаров
    products_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for product_id in products_to_add:
        wait.until(EC.element_to_be_clickable((By.ID, product_id))).click()

    # 4. Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 5. Нажатие Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # 6. Заполнение формы
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Иванов")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    # 7. Continue
    driver.find_element(By.ID, "continue").click()

    # 8. Получение суммы
    total = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
    total_value = float(total.replace("Total: $", ""))
    
    # 10. Проверка
    assert total_value == 58.29, f"Ожидалось $58.29, но было ${total_value}"

finally:
    # 9. Закрытие браузера
    driver.quit()
