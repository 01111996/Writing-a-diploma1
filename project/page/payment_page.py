import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from project.page.base_page import BasePage

class PaymentPage(BasePage):
    CARD_NUMBER  = (By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
    EXPIRY_MONTH = (By.CSS_SELECTOR, "input[placeholder='Месяц']")
    EXPIRY_YEAR  = (By.CSS_SELECTOR, "input[placeholder='Год']")
    OWNER_NAME   = (By.CSS_SELECTOR, "input[placeholder='Владелец']")
    CVC          = (By.CSS_SELECTOR, "input[placeholder='CVC/CVV']")
    PAY_BUTTON   = (By.XPATH, "//button[contains(., 'Продолжить')]")

    def fill_card(self, card_data):
        self.find(self.CARD_NUMBER).send_keys(card_data["number"])
        time.sleep(0.5)
        self.find(self.EXPIRY_MONTH).send_keys(card_data["month"])
        self.find(self.EXPIRY_YEAR).send_keys(card_data["year"])
        self.find(self.OWNER_NAME).send_keys(card_data["owner"])
        self.find(self.CVC).send_keys(card_data["cvc"])
        
    def pay(self):
        self.find(self.PAY_BUTTON).click()