from selenium.webdriver.common.by import By
from project.page.base_page import BasePage

class PaymentPage(BasePage):
    CARD_NUMBER  = (By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
    EXPIRY_MONTH = (By.CSS_SELECTOR, "input[placeholder='06']")
    EXPIRY_YEAR  = (By.CSS_SELECTOR, "input[placeholder='27']")
    OWNER_NAME   = (By.XPATH, "(//fieldset//input)[4]")
    CVC          = (By.CSS_SELECTOR, "input[placeholder='357']")
    PAY_BUTTON   = (By.XPATH, "//button[normalize-space()='Продолжить']")
    SUCCESS_MSG  = (By.XPATH, "//*[contains(text(),'Операция одобрена')]")
    ERROR_MSG    = (By.XPATH, "//*[contains(text(),'Ошибка')]")

    def fill_card(self, card_number, month, year, owner, cvc):
        self.find(self.CARD_NUMBER).send_keys(card_number)
        self.find(self.EXPIRY_MONTH).send_keys(month)
        self.find(self.EXPIRY_YEAR).send_keys(year)
        self.find(self.OWNER_NAME).send_keys(owner)
        self.find(self.CVC).send_keys(cvc)
        self.find(self.PAY_BUTTON).click()