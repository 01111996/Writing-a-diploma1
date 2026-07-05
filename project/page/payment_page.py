from selenium.webdriver.common.by import By
from project.page.base_page import BasePage

class PaymentPage(BasePage):
    CARD_NUMBER = (By.ID, "card-number")
    EXPIRY_MONTH = (By.ID, "expiry-month")
    EXPIRY_YEAR = (By.ID, "expiry-year")
    OWNER_NAME = (By.ID, "card-owner")
    CVC = (By.ID, "cvc")
    PAY_BUTTON = (By.ID, "pay-button")
    TRANSACTION_SELECT = (By.CLASS_NAME, "form-control")  
    PURCHASE_OPTION = (By.XPATH, "//option[text()='Покупка']")
    CREDIT_OPTION = (By.XPATH, "//option[text()='Кредит']")

    def choose_transaction_type(self, transaction_type: str):
        dropdown = self.find(self.TRANSACTION_SELECT)
        dropdown.click()  

        if transaction_type == "purchase":
            option = self.find(self.PURCHASE_OPTION)
        elif transaction_type == "credit":
            option = self.find(self.CREDIT_OPTION)
        else:
            raise ValueError("Invalid transaction type")

        option.click()

    def fill_card(self, card_data):
        self.choose_transaction_type(card_data.get("transaction_type", "purchase"))
        self.find(self.CARD_NUMBER).clear()
        self.find(self.CARD_NUMBER).send_keys(card_data["number"])
        self.find(self.EXPIRY_MONTH).send_keys(card_data["month"])
        self.find(self.EXPIRY_YEAR).send_keys(card_data["year"])
        self.find(self.OWNER_NAME).send_keys(card_data["owner"])
        self.find(self.CVC).send_keys(card_data["cvc"])

    def pay(self):
        self.find(self.PAY_BUTTON).click()