import pytest
from page.main_pages import MainPages
from page.base_pages import BasePages
from page.payment_pages import PaymentPages
from data.cards import APPROVED_CARD, DECLINED_CARD, MISSING_NUMBER_CARD, WITHOUT_CARD, CVC_CARD, CVC1_CARD, CYRILLIC_CARD, F_CARD, N_CARD

#Отклонено
def test_payment_with_declined_card(driver):
    main_page = MainPages(driver)
    main_page.open()
    main_page.click_buy()
    base_page = BasePages(driver)
    base_page.fill_card(DECLINED_CARD)
    base_page.pay()
    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert 'Отклонено' in actual_result

#•	При покупке тура по дебетовой карте происходит ошибка: 
# клиент вводит актуальные данные карты, средств на карте достаточно, 
# но происходит отказ. (негативный сценарий)
def test_payment_error(driver):
    main_page = MainPages(driver)
    payment_page = PaymentPages(driver)
    main_page.open()
    main_page.click_buy()
    payment_page.fill_card(APPROVED_CARD)
    payment_page.pay()
    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert 'Ошибка' in actual_result
    
#•	Все поля пустые, нет возможности отправить заявку
def test_submit_empty_form_shows_error(driver):
    main_page = MainPages(driver)
    payment_page = PaymentPages(driver)
    main_page.open()           
    main_page.click_buy()      
    payment_page.pay()
    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert 'Ошибка' in actual_result, f"Ожидалось увидеть ошибку, но получили '{actual_result}'"

#Номер карты менее 16 цифр
def test_payment_with_missing_number_card(driver):
    main_page = MainPages(driver)
    payment_page = PaymentPages(driver)
    main_page.open()
    main_page.click_buy()
    payment_page.fill_card(MISSING_NUMBER_CARD)
    payment_page.pay()
    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert 'Ошибка' in actual_result

#Пустое поле "Номер карты"
def test_payment_with_without_card(driver):
    main_page = MainPages(driver)
    payment_page = PaymentPages(driver)
    main_page.open()
    main_page.click_buy()
    payment_page.fill_card(WITHOUT_CARD)
    payment_page.pay()
    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert 'Ошибка' in actual_result

#•	CVC менее, чем три цифры
def test_payment_with_cvc_card(driver):
    main_page = MainPages(driver)
    payment_page = PaymentPages(driver)
    main_page.open()
    main_page.click_buy()
    payment_page.fill_card(CVC_CARD)
    payment_page.pay()
    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert 'Ошибка' in actual_result

#Пустое CVC
def test_payment_with_cvc1_card(driver):
    main_page = MainPages(driver)
    payment_page = PaymentPages(driver)
    main_page.open()
    main_page.click_buy()
    payment_page.fill_card(CVC1_CARD)
    payment_page.pay()
    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert 'Ошибка' in actual_result

#ФИО на кириллице
def test_payments_with_cyrillic_card(driver):
    main_page = MainPages(driver)
    payment_page = PaymentPages(driver)
    main_page.open()
    main_page.click_buy()
    payment_page.fill_card(CYRILLIC_CARD)
    payment_page.pay()
    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert 'Ошибка' in actual_result   

#Пустое поле "Фамилия"
def test_payments_with_f_card(driver):
    main_page = MainPages(driver)
    payment_page = PaymentPages(driver)
    main_page.open()
    main_page.click_buy()
    payment_page.fill_card(F_CARD)
    payment_page.pay()
    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert 'Ошибка' in actual_result 

#   Пустое поле "Имя"   
def test_payments_with_n_card(driver):
    main_page = MainPages(driver)
    payment_page = PaymentPages(driver)
    main_page.open()
    main_page.click_buy()
    payment_page.fill_card(N_CARD)
    payment_page.pay()
    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert 'Ошибка' in actual_result 