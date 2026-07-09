import pytest
from project.page.main_page import MainPage
from project.page.payment_page import PaymentPage
from project.data.cards import TestCard
from project.helpers.notification_helper import NotificationHelper
from project.assertions import Assertions

#Отклонено
def test_payment_with_declined_card(driver):
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page(mode="buy")
    payment_page.fill_card(TestCard.DECLINED_CARD)
    payment_page.click_buy_button()
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_declined_notification(actual_result)

#•	При покупке тура по дебетовой карте происходит ошибка: 
# клиент вводит актуальные данные карты, средств на карте достаточно, 
# но происходит отказ. (негативный сценарий)
@pytest.mark.xfail(reason="Bug: приложение отклоняет одобренную карту", strict=False) #баг?
def test_payment_error(driver):
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page(mode="buy")
    payment_page.fill_card(TestCard.APPROVED_CARD)
    payment_page.click_buy_button()
    actual_result = NotificationHelper.get_notification_text(driver)
    Assertions.assert_error_notification(actual_result)
    
#•	Все поля пустые, нет возможности отправить заявку
def test_submit_empty_form_shows_error(driver):
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page()
    button = payment_page.find(PaymentPage.BUY_BUTTON)
    assert not button.is_enabled(), "Кнопка дне активна для нажатия без введения данных"

#Номер карты менее 16 цифр
def test_payment_with_missing_number_card(driver):
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page(mode="buy")
    payment_page.fill_card(TestCard.MISSING_NUMBER_CARD)
    payment_page.click_buy_button()
    actual_result = NotificationHelper.get_field_error_text(driver)
    Assertions.assert_field_error(actual_result)

#Пустое поле "Номер карты"
def test_payment_with_without_card(driver):
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page(mode="buy")
    payment_page.fill_card(TestCard.WITHOUT_CARD)
    payment_page.click_buy_button()
    actual_result = NotificationHelper.get_field_error_text(driver)
    Assertions.assert_field_error(actual_result)

#•	CVC менее, чем три цифры
def test_payment_with_cvc_card(driver):
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page(mode="buy")
    payment_page.fill_card(TestCard.CVC_CARD)
    payment_page.click_buy_button()
    actual_result = NotificationHelper.get_field_error_text(driver)
    Assertions.assert_field_error(actual_result)

#Пустое CVC
def test_payment_with_cvc1_card(driver):
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page(mode="buy")
    payment_page.fill_card(TestCard.CVC1_CARD)
    payment_page.click_buy_button()
    actual_result = NotificationHelper.get_field_error_text(driver)
    Assertions.assert_field_error(actual_result)

#ФИО на кириллице
def test_payments_with_cyrillic_card(driver):
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page(mode="buy")
    payment_page.fill_card(TestCard.CYRILLIC_CARD)
    payment_page.click_buy_button()
    actual_result = NotificationHelper.get_field_error_text(driver)
    Assertions.assert_field_error(actual_result)   

#Пустое поле "Фамилия"
@pytest.mark.xfail(reason="Приложение не проверяет наличие фамилии", strict=False) #баг?
def test_payments_with_f_card(driver):
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page(mode="buy")
    payment_page.fill_card(TestCard.F_CARD)
    payment_page.click_buy_button()
    actual_result = NotificationHelper.get_field_error_text(driver)
    Assertions.assert_field_error(actual_result)  

#   Пустое поле "Имя"   
@pytest.mark.xfail(reason="Приложение не проверяет наличие имени", strict=False) #баг?
def test_payments_with_n_card(driver):
    main_page = MainPage(driver)
    payment_page = main_page.go_to_payment_page(mode="buy")
    payment_page.fill_card(TestCard.N_CARD)
    payment_page.click_buy_button()
    actual_result = NotificationHelper.get_field_error_text(driver)
    Assertions.assert_field_error(actual_result)