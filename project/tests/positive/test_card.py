#•	Покупка тура дебетовой картой: покупатель заходит на сайт, вводит данные карты, 
# оплачивает. (позитивный сценарий)

import pytest
from project.page.main_page import MainPage
from project.page.payment_page import PaymentPage
from data.cards import TestCard

#Одобрено
def test_payment_with_approved_card(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_buy()
    base_page = PaymentPage(driver)
    base_page.fill_card(TestCard.APPROVED_CARD) 
    base_page.pay()
    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert 'Успешно' in actual_result
