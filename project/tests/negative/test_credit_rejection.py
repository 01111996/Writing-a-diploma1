import pytest
from page.main_pages import MainPages
from page.base_pages import BasePages
from page.payment_pages import PaymentPages
from data.cards import DECLINED_CARD

#•	При оформлении кредита на тур происходит отказ. (негативный сценарий)
def test_credit_rejection(driver):
    driver.get("http://localhost:8080")
    main_pages = MainPages(driver)
    main_pages.click_credit()

    payment_page = PaymentPages(driver)
    payment_page.fill_card(DECLINED_CARD)
    payment_page.pay()

    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert "Отказ" in actual_result or "Отклонено" in actual_result