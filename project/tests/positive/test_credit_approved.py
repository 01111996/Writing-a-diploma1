#•	Покупка кредита: покупатель заходит на сайт, 
# оформляет тур в кредит. (позитивный сценарий)
import pytest
import logging
from project.page.main_page import MainPage
from project.page.payment_page import PaymentPage
from project.data.cards import TestCard
from project.helpers.notification_helper import NotificationHelper
from project.assertions import Assertions
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

def test_credit(driver, assert_db_status_success):
    logger.info("Открывается страница для покупки тура в кредит")
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page()
    logger.info("Заполняется данными APPROVED_CARD")
    payment_page.fill_card(TestCard.APPROVED_CARD)
    order_id = datetime.now(timezone.utc) 
    logger.info("Нажимается кнопка 'Продолжить'")
    payment_page.click_credit_button()
    logger.info("Проверяется уведомление об одобрении кредита")
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_approved_notification(actual_result)
    logger.info("Проверяется статус кредитной заявки в БД")
    assert_db_status_success(order_id, table="credit_request_entity")

    