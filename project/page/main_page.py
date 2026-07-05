from project.page.base_page import BasePage
from project.page.payment_page import PaymentPage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    BUY_BUTTON = (By.ID, 'buy-button') 
    CREDIT_BUTTON = (By.ID, 'credit-button') 

    def click_buy(self):
        self.find(self.BUY_BUTTON).click()

    def click_credit(self):
        self.find(self.CREDIT_BUTTON).click()

    def open(self):
        self.driver.get('http://localhost:8080/')

    def go_to_payment_page(self, mode="buy"):
        if mode == "buy":
            self.click_buy()
        elif mode == "credit":
            self.click_credit()
        else:
            raise ValueError("Invalid mode")
        return PaymentPage(self.driver)

    