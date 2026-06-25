from selenium.webdriver.common.by import By
from project.page.base_page import BasePage

class PaymentPage(BasePage):
    CARD_NUMBER = (By.ID, 'card-number')
    EXPIRY_MONTH = (By.ID, 'expiry-month')
    EXPIRY_YEAR = (By.ID, 'expiry-year')
    OWNER_NAME = (By.ID, 'card-owner')
    CVC = (By.ID, 'cvc')
    PAY_BUTTON = (By.ID, 'pay-button') 

    def fill_card(self, card_data):
        self.find(self.CARD_NUMBER).send_keys(card_data['number'])
        self.find(self.EXPIRY_MONTH).send_keys(card_data['month'])
        self.find(self.EXPIRY_YEAR).send_keys(card_data['year'])
        self.find(self.OWNER_NAME).send_keys(card_data['owner'])
        self.find(self.CVC).send_keys(card_data['cvc'])

    def pay(self):
        self.find(self.PAY_BUTTON).click()