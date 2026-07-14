#•	Покупка тура дебетовой картой: покупатель заходит на сайт, вводит данные карты, 
# оплачивает. (позитивный сценарий)

import pytest
import logging
from project.page.main_page import MainPage
from project.page.payment_page import PaymentPage
from project.data.cards import TestCard
from project.helpers.notification_helper import NotificationHelper
from project.assertions import Assertions
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

def test_payment_with_approved_card(driver, assert_db_status_success):
    logger.info("Открывается страница для оплаты дебетовой картой")
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page(mode="buy")
    logger.info("Заполняется данными APPROVED_CARD")
    payment_page.fill_card(TestCard.APPROVED_CARD)
    order_id = datetime.now(timezone.utc)  
    payment_page.click_buy_button()
    logger.info("Проверка наличия ведомления об успешной оплате")
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_approved_notification(actual_result)
    logger.info("Проверка статуса платежа в БД")
    assert_db_status_success(order_id)
