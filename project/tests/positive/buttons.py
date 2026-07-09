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

    assert buy_button.is_displayed() and buy_button.is_enabled(), \
        "Кнопка 'Купить' должна быть видна и активна"
    
    assert credit_button.is_displayed() and credit_button.is_enabled(), \
        "Кнопка 'Купить в кредит' должна быть видна и активна"

    buy_button.click()
    payment_page = PaymentPage(driver)
    card_field = payment_page.find(PaymentPage.CARD_NUMBER)

    assert card_field.is_displayed(), \
        "После нажатия 'Купить' должно появиться поле ввода номера карты"

    credit_button = main_page.find(MainPage.CREDIT_BUTTON)
    credit_button.click()
    card_field = payment_page.find(PaymentPage.CARD_NUMBER)
    
    assert card_field.is_displayed(), \
        "После нажатия 'Купить в кредит' должно появиться поле ввода номера карты"