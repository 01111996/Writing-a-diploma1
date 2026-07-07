import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from project.page.base_page import BasePage

class PaymentPage(BasePage):
    CARD_NUMBER = (By.XPATH, "//input[@placeholder='0000 0000 0000 0000']")
    EXPIRY_MONTH = (By.XPATH, "//label[normalize-space()='Месяц']/following::input[1]")
    EXPIRY_YEAR  = (By.XPATH, "//label[normalize-space()='Год']/following::input[1]")
    OWNER_NAME   = (By.XPATH, "//label[normalize-space()='Владелец']/following::input[1]")
    CVC          = (By.XPATH, "//label[contains(normalize-space(),'CVC')]/following::input[1]")
    PAY_BUTTON   = (By.XPATH, "//button[contains(normalize-space(),'Продолжить') or contains(normalize-space(),'Отправить')]")
    
    def fill_card(self, card_data):
        number_field = self.wait.until(EC.presence_of_element_located(self.CARD_NUMBER))
        number_field.clear()
        number_field.send_keys(card_data["number"])
        time.sleep(1)
        self.find(self.EXPIRY_MONTH).send_keys(card_data["month"])
        self.find(self.EXPIRY_YEAR).send_keys(card_data["year"])
        self.find(self.OWNER_NAME).send_keys(card_data["owner"])
        self.find(self.CVC).send_keys(card_data["cvc"])
        
    def pay(self):
        self.find(self.PAY_BUTTON).click()