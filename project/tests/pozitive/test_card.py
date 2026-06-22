#•	Покупка тура дебетовой картой: покупатель заходит на сайт, вводит данные карты, 
# оплачивает. (позитивный сценарий)

import pytest
from page.main_pages import MainPages
from page.base_pages import BasePages
from page.payment_pages import PaymentPages
from data.cards import APPROVED_CARD

#Одобрено
def test_payment_with_approved_card(driver):
    main_pages = MainPages(driver)
    main_pages.open()
    main_pages.click_buy()
    base_pages = BasePages(driver)
    base_pages.fill_card(APPROVED_CARD) 
    base_pages.pay()
    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert 'Успешно' in actual_result
