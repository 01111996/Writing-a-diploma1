#•	Покупка кредита: покупатель заходит на сайт, 
# оформляет тур в кредит. (позитивный сценарий)
import pytest
from page.main_pages import MainPages
from page.base_pages import BasePages
from page.payment_pages import PaymentPages
from data.cards import APPROVED_CARD

def test_credit(driver):
    driver.get("http://localhost:8080")
    main_pages = MainPages(driver)
    main_pages.click_credit()

    payment_pages = PaymentPages(driver)
    payment_pages.fill_card_data(APPROVED_CARD)
    payment_pages.submit()

    assert "Одобрено" in driver.page_source

    