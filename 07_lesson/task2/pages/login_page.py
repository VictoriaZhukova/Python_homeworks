from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://www.saucedemo.com/"
    
    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(self.URL)
    
    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)
    
    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()
