#•	Покупка кредита: покупатель заходит на сайт, 
# оформляет тур в кредит. (позитивный сценарий)
import pytest
from project.page.main_page import MainPage
from project.page.payment_page import PaymentPage
from data.cards import TestCard

def test_credit(driver):
    driver.get("http://localhost:8080")
    main_pages = MainPage(driver)
    main_pages.click_credit()
    payment_pages = PaymentPage(driver)
    payment_pages.fill_card(TestCard.APPROVED_CARD)
    payment_pages.pay()
    assert "Одобрено" in driver.page_source

    