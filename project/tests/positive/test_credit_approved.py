#•	Покупка кредита: покупатель заходит на сайт, 
# оформляет тур в кредит. (позитивный сценарий)
import pytest
from project.page.main_page import MainPage
from project.page.payment_page import PaymentPage
from project.data.cards import TestCard
from project.helpers.notification_helper import NotificationHelper

def test_credit(driver):
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page()
    payment_page.fill_card(TestCard.APPROVED_CARD)
    payment_page.pay()
    actual = NotificationHelper.get_notification_text(driver)
    Assertions.assert_approved_notification(actual)

    