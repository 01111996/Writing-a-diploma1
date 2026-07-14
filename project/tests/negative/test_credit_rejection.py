import pytest
import logging
from project.page.main_page import MainPage
from project.page.payment_page import PaymentPage
from project.data.cards import TestCard
from project.helpers.notification_helper import NotificationHelper
from project.assertions import Assertions

logger = logging.getLogger(__name__)

#•	При оформлении кредита на тур происходит отказ. (негативный сценарий)
def test_credit_rejection(driver):
    logger.info("Открывается страница для покупки тура в кредит")
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page()
    logger.info("Заполняется данными DECLINED_CARD")
    payment_page.fill_card(TestCard.DECLINED_CARD)
    logger.info("Нажимается кнопка 'Продолжить'")
    payment_page.click_credit_button()
    logger.info("Проверяется уведомление об ошибке")
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_declined_notification(actual_result)