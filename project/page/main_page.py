from project.page.base_page import BasePage
from project.page.payment_page import PaymentPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    BUY_BUTTON = (By.XPATH, "//button[normalize-space()='Купить']")
    CREDIT_BUTTON = (By.XPATH, "//button[normalize-space()='Купить в кредит']")

    def click_buy(self):
        button = self.wait.until(EC.presence_of_element_located(self.BUY_BUTTON))
        button = self.wait.until(EC.element_to_be_clickable(button))
        button.click()

    def click_credit(self):
        button = self.wait.until(EC.presence_of_element_located(self.CREDIT_BUTTON))
        button = self.wait.until(EC.element_to_be_clickable(button))
        button.click()

    def open(self):
        self.driver.get('http://localhost:8080/')
        
    def go_to_payment_page(self, mode="credit"):
        if mode == "buy":
            self.click_buy()
        else:
            self.click_credit()
        return PaymentPage(self.driver)

    