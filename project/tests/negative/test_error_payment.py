import pytest
import logging
from project.data.cards import TestCard
from project.helpers.notification_helper import NotificationHelper
from project.helpers.payment_helper import perform_payment
from project.assertions import Assertions

logger = logging.getLogger(__name__)

#Отклонено
def test_payment_with_declined_card(driver, assert_db_status_success):
    order_id = perform_payment(driver, TestCard.DECLINED_CARD, mode="buy")
    logger.info("Проверяется наличие уведомления об отказе")
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_declined_notification(actual_result)
    logger.info("Проверяется статус платежа в БД")
    assert_db_status_success(order_id, expected_status="DECLINED", table="payment_entity")
    
#•	Все поля пустые, нет возможности отправить заявку
def test_submit_empty_form_shows_error(driver):
    perform_payment(driver, {"number": "", "month": "", "year": "", "owner": "", "cvc": ""}, mode="buy")
    logger.info("Проверяется ошибка валидации не заполненной формы данных по карте")
    actual_result = NotificationHelper.get_field_error_text(driver)
    Assertions.assert_field_error(actual_result)


#Номер карты менее 16 цифр
def test_payment_with_missing_number_card(driver):
    perform_payment(driver, TestCard.MISSING_NUMBER_CARD, mode="buy")
    logger.info("Проверяется ошибка валидации: короткий номер карты")
    actual_result = NotificationHelper.get_field_error_text(driver)
    Assertions.assert_field_error(actual_result)

#Пустое поле "Номер карты"
def test_payment_with_without_card(driver):
    perform_payment(driver, TestCard.WITHOUT_CARD, mode="buy")
    logger.info("Проверяется ошибка валидации: отсутствие номера карты")
    actual_result = NotificationHelper.get_field_error_text(driver)
    Assertions.assert_field_error(actual_result)

#•	CVC менее, чем три цифры
def test_payment_with_cvc_card(driver):
    perform_payment(driver, TestCard.CVC_CARD, mode="buy")
    logger.info("Проверяется ошибка валидации: короткий CVC")
    actual_result = NotificationHelper.get_field_error_text(driver)
    Assertions.assert_field_error(actual_result)

#Пустое CVC
def test_payment_with_cvc1_card(driver):
    perform_payment(driver, TestCard.CVC1_CARD, mode="buy")
    logger.info("Проверяется ошибка валидации: отсутствие CVC")
    actual_result = NotificationHelper.get_field_error_text(driver)
    Assertions.assert_field_error(actual_result, expected_text='Поле обязательно для заполнения')

#ФИО на кириллице
def test_payments_with_cyrillic_card(driver):
    perform_payment(driver, TestCard.CYRILLIC_CARD, mode="buy")
    logger.info("Проверяется ошибка валидации: кириллица в ФИО")
    actual_result = NotificationHelper.get_field_error_text_safe(driver)
    Assertions.assert_field_error(actual_result)  

#Пустое поле "Фамилия"
def test_payments_with_f_card(driver):
    perform_payment(driver, TestCard.F_CARD, mode="buy")
    logger.info("Проверяется ошибка валидации: отсутствие фамилии")
    actual_result = NotificationHelper.get_field_error_text_safe(driver)
    Assertions.assert_field_error(actual_result)

#   Пустое поле "Имя"   
def test_payments_with_n_card(driver):
    perform_payment(driver, TestCard.N_CARD, mode="buy")
    logger.info("Проверяется ошибка валидации: отсутствие имени")
    actual_result = NotificationHelper.get_field_error_text_safe(driver)
    Assertions.assert_field_error(actual_result)