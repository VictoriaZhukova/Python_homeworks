from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
    
    def fill_info(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    
    def click_continue(self):
        self.driver.find_element(By.ID, "continue").click()
        # Ждем загрузки страницы Overview с итоговой суммой
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
    
    def get_total_price(self):
        total_text = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        # Формат: "Total: $58.29"
        return float(total_text.split('$')[1])
