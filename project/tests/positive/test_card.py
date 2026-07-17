#•	Покупка тура дебетовой картой: покупатель заходит на сайт, вводит данные карты, 
# оплачивает. (позитивный сценарий)

import logging
from project.data.cards import TestCard
from project.helpers.notification_helper import NotificationHelper
from project.helpers.payment_helper import perform_payment
from project.assertions import Assertions

logger = logging.getLogger(__name__)

def test_payment_with_approved_card(driver, assert_db_status_success):
    order_id = perform_payment(driver, TestCard.APPROVED_CARD, mode="buy")
    logger.info("Проверяется уведомление об успешной оплате")
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_approved_notification(actual_result)
    logger.info("Проверяется статус платежа в БД")
    assert_db_status_success(order_id)
