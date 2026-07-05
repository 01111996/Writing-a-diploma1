#•	Покупка тура дебетовой картой: покупатель заходит на сайт, вводит данные карты, 
# оплачивает. (позитивный сценарий)

import pytest
from project.page.main_page import MainPage
from project.page.payment_page import PaymentPage
from project.data.cards import TestCard
from project.helpers.notification_helper import NotificationHelper
from project.assertions import Assertions

#Одобрено
def test_payment_with_approved_card(driver):
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page(mode="buy")
    payment_page.fill_card(TestCard.APPROVED_CARD)
    payment_page.pay()
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_error_notification(actual_result, expected_text="Успешно")
