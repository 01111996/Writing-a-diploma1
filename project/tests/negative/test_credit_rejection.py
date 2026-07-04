import pytest
from project.page.main_page import MainPage
from project.page.payment_page import PaymentPage
from project.data.cards import TestCard

#•	При оформлении кредита на тур происходит отказ. (негативный сценарий)
def test_credit_rejection(driver):
    driver.get("http://localhost:8080")
    main_pages = MainPage(driver)
    main_pages.click_credit()

    payment_page = PaymentPage(driver)
    payment_page.fill_card(TestCard.DECLINED_CARD)
    payment_page.pay()

    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert "Отказ" in actual_result or "Отклонено" in actual_result