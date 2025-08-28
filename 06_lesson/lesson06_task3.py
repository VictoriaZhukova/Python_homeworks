from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждем появления минимум 3 картинок на странице
    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3
    )
    
    # Ждем, пока все картинки загрузятся (naturalWidth > 0)
    WebDriverWait(driver, 10).until(
        lambda d: all(
            img.get_attribute("naturalWidth") != '0'
            for img in d.find_elements(By.TAG_NAME, "img")
        )
    )
    
    third_img = driver.find_elements(By.TAG_NAME, "img")[2]
    src_value = third_img.get_attribute("src")
    print(src_value)

finally:
    driver.quit()
    