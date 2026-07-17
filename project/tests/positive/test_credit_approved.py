#•	Покупка кредита: покупатель заходит на сайт, 
# оформляет тур в кредит. (позитивный сценарий)

import logging
from project.data.cards import TestCard
from project.helpers.notification_helper import NotificationHelper
from project.helpers.payment_helper import perform_payment
from project.assertions import Assertions

logger = logging.getLogger(__name__)

def test_credit(driver, assert_db_status_success):
    order_id = perform_payment(driver, TestCard.APPROVED_CARD, mode="credit")
    logger.info("Проверяется уведомление об одобрении кредита")
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_approved_notification(actual_result)
    logger.info("Проверяется статус кредитной заявки в БД")
    assert_db_status_success(order_id, table="credit_request_entity")

    