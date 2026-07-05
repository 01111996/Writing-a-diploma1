from project.page.base_page import BasePage
from project.page.payment_page import PaymentPage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    BUY_BUTTON = (By.ID, "button-book") 

    def click_buy(self):
        button = self.wait.until(EC.element_to_be_clickable(self.BUY_BUTTON))
        button.click()

    def click_credit(self):
        self.find(self.CREDIT_BUTTON).click()

    def open(self):
        self.driver.get('http://localhost:8080/')

    def go_to_payment_page(self):
        self.click_buy()
        return PaymentPage(self.driver)

    