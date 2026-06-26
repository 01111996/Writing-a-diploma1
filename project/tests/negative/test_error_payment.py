import pytest
from project.page.main_page import MainPage
from project.page.base_page import BasePage
from project.page.payment_page import PaymentPage
from data.cards import TestCard
from helpers.notification_helper import NotificationHelper
from assertion import Assertions

#Отклонено
def test_payment_with_declined_card(driver):
    main_page = MainPage(driver)
    base_page = BasePage(driver)
    main_page.open()
    main_page.click_buy()
    base_page.fill_card(DECLINED_CARD)
    base_page.pay()
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_declined_notification(actual_result)

#•	При покупке тура по дебетовой карте происходит ошибка: 
# клиент вводит актуальные данные карты, средств на карте достаточно, 
# но происходит отказ. (негативный сценарий)
def test_payment_error(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)
    main_page.open()
    main_page.click_buy()
    payment_page.fill_card(APPROVED_CARD)
    payment_page.pay()
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_error_notification(actual_result)
    
#•	Все поля пустые, нет возможности отправить заявку
def test_submit_empty_form_shows_error(driver):
    payment_page = payment_page_setup
    payment_page.pay() 
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_error_notification(actual_result)

#Номер карты менее 16 цифр
def test_payment_with_missing_number_card(payment_page, driver):
    payment_page = payment_page_setup
    payment_page.fill_card(MISSING_NUMBER_CARD)
    payment_page.pay()
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_error_notification(actual_result)

#Пустое поле "Номер карты"
def test_payment_with_without_card(payment_page, driver):
    payment_page = payment_page_setup
    payment_page.fill_card(WITHOUT_CARD)
    payment_page.pay()
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_error_notification(actual_result)

#•	CVC менее, чем три цифры
def test_payment_with_cvc_card(payment_page, driver):
    payment_page = payment_page_setup
    payment_page.fill_card(CVC_CARD)
    payment_page.pay()
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_error_notification(actual_result)

#Пустое CVC
def test_payment_with_cvc1_card(payment_page, driver):
    payment_page = payment_page_setup
    payment_page.fill_card(CVC1_CARD)
    payment_page.pay()
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_error_notification(actual_result)

#ФИО на кириллице
def test_payments_with_cyrillic_card(payment_page, driver):
    payment_page = payment_page_setup
    payment_page.fill_card(CYRILLIC_CARD)
    payment_page.pay()
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_error_notification(actual_result)   

#Пустое поле "Фамилия"
def test_payments_with_f_card(payment_page, driver):
    payment_page = payment_page_setup
    payment_page.fill_card(F_CARD)
    payment_page.pay()
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_error_notification(actual_result)  

#   Пустое поле "Имя"   
def test_payments_with_n_card(payment_page, driver):
    payment_page = payment_page_setup
    payment_page.fill_card(N_CARD)
    payment_page.pay()
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_error_notification(actual_result)