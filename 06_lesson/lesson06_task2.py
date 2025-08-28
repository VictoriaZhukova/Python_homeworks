from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


try:
    driver.get("http://uitestingplayground.com/textinput")
    
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")
    
    button = driver.find_element(By.ID, "updatingButton")
    original_text = button.text
    button.click()
    
    # Ждем, пока текст кнопки изменится
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.ID, "updatingButton").text != original_text
    )
    
    updated_text = driver.find_element(By.ID, "updatingButton").text
    print(updated_text)

finally:
    driver.quit()
    