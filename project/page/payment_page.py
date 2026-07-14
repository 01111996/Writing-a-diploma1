from selenium.webdriver.common.by import By
from project.page.base_page import BasePage

class PaymentPage(BasePage):
    CARD_NUMBER     = (By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
    EXPIRY_MONTH    = (By.CSS_SELECTOR, "input[placeholder='08']")
    EXPIRY_YEAR     = (By.CSS_SELECTOR, "input[placeholder='22']")
    CVC             = (By.CSS_SELECTOR, "input[placeholder='999']")
    OWNER_NAME      = (By.XPATH, "//span[text()='Владелец']/following::input[1]") 
    BUY_BUTTON      = (By.XPATH, "//button[normalize-space()='Купить']")
    CREDIT_BUTTON   = (By.XPATH, "//button[normalize-space()='Купить в кредит']")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(., 'Продолжить')]")
    SUCCESS_MSG     = (By.XPATH, "//*[contains(text(),'Успешно')]")
    ERROR_MSG       = (By.XPATH, "//*[contains(text(),'Ошибка')]")

    def fill_card(self, card: dict):
        self.find(self.CARD_NUMBER).send_keys(card["number"])
        self.find(self.EXPIRY_MONTH).send_keys(card["month"])
        self.find(self.EXPIRY_YEAR).send_keys(card["year"])
        self.find(self.OWNER_NAME).send_keys(card["owner"])
        self.find(self.CVC).send_keys(card["cvc"])

    def click_buy_button(self): #для дебетовой карты
        self.find(self.CONTINUE_BUTTON).click()

    def click_credit_button(self): #для кредита
        self.find(self.CONTINUE_BUTTON).click()