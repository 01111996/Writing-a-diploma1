import logging
from project.data.cards import TestCard
from project.helpers.notification_helper import NotificationHelper
from project.helpers.payment_helper import perform_payment
from project.assertions import Assertions
logger = logging.getLogger(__name__)

#•	При оформлении кредита на тур происходит отказ. (негативный сценарий)
def test_credit_rejection(driver, assert_db_status_success):
    order_id = perform_payment(driver, TestCard.DECLINED_CARD, mode="credit")
    logger.info("Проверяется уведомление об отказе в кредите")
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_declined_notification(actual_result)
    logger.info("Проверяется статус кредитной заявки в БД")
    assert_db_status_success(order_id, expected_status="DECLINED", table="credit_request_entity")