from selenium.webdriver.common.by import By
from project.page.base_page import BasePage

class PaymentPage(BasePage):
    CARD_NUMBER  = (By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
    EXPIRY_MONTH = (By.XPATH, "//span[text()='Месяц']/following::input[1]")
    EXPIRY_YEAR  = (By.XPATH, "//span[text()='Год']/following::input[1]")
    OWNER_NAME   = (By.XPATH, "//span[text()='Владелец']/following::input[1]")
    CVC          = (By.XPATH, "//span[text()='CVC/CVV']/following::input[1]")
    PAY_BUTTON   = (By.XPATH, "//button[normalize-space()='Продолжить']")
    SUCCESS_MSG  = (By.XPATH, "//*[contains(text(),'Успешно')]")
    ERROR_MSG    = (By.XPATH, "//*[contains(text(),'Ошибка')]")

    def fill_card(self, card: dict):
        self.find(self.CARD_NUMBER).send_keys(card["number"])
        self.find(self.EXPIRY_MONTH).send_keys(card["month"])
        self.find(self.EXPIRY_YEAR).send_keys(card["year"])
        self.find(self.OWNER_NAME).send_keys(card["owner"])
        self.find(self.CVC).send_keys(card["cvc"])
        
    def pay(self):
        self.find(self.PAY_BUTTON).click()