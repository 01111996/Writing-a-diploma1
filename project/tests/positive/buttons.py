#•	Активные кнопки «Купить» и «Купить в кредит»:
#  переключение между кнопками происходит без ошибок. (позитивный сценарий)

import pytest
from project.page.main_page import MainPage
from project.page.payment_page import PaymentPage

def test_active_buttons(driver):
    main_page = MainPage(driver)
    main_page.open()
    buy_button = main_page.find(MainPage.BUY_BUTTON)
    credit_button = main_page.find(MainPage.CREDIT_BUTTON)
    buy_button.click()
    assert "Успешно" in driver.page_source
    credit_button.click()
    assert "Кредит оформлен" in driver.page_source