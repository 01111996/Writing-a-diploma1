import pytest
from project.page.main_page import MainPage
from project.page.payment_page import PaymentPage
from project.data.cards import TestCard
from project.helpers.notification_helper import NotificationHelper
from project.assertions import Assertions

#•	При оформлении кредита на тур происходит отказ. (негативный сценарий)
def test_credit_rejection(driver):
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page(mode="credit")
    payment_page.fill_card(TestCard.DECLINED_CARD)
    payment_page.pay()
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_declined_notification(actual_result)