from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation_edge():
    # Укажи путь к msedgedriver.exe — обязательно скачай драйвер и положи по этому пути
    edge_service = EdgeService(executable_path="C:/WebDriver/msedgedriver.exe")
    edge_options = Options()

    driver = webdriver.Edge(service=edge_service, options=edge_options)
    wait = WebDriverWait(driver, 10)

    try:
        url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        driver.get(url)

        # Заполняем поля
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")

        # Явное ожидание появления поля email
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "e-mail")))
        email_field.send_keys("test@skypro.com")

        driver.find_element(By.NAME, "phone").send_keys("+798589998787")
        # Zip оставляем пустым
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Нажимаем кнопку Submit
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Ждём, пока форма получит класс 'was-validated'
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "was-validated")))

        # Проверка: Zip должен быть подсвечен как невалидный
        zip_code = driver.find_element(By.NAME, "zip")
        assert "is-invalid" in zip_code.get_attribute("class"), "Zip code не подсвечено красным"

        # Проверка остальных полей — должны быть валидны
        valid_fields = [
            "first-name", "last-name", "address", "email", "phone",
            "city", "country", "job-position", "company"
        ]
        for field_name in valid_fields:
            field = driver.find_element(By.NAME, field_name)
            assert "is-valid" in field.get_attribute("class"), f"Поле {field_name} не подсвечено зелёным"

    finally:
        driver.quit()

