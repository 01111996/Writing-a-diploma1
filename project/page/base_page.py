from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def fill_card(self, card_data):
        self.find((By.ID, 'card-number')).send_keys(card_data['number'])

    def pay(self):
        self.find((By.ID, 'pay-button')).click()