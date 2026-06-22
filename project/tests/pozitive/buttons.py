#•	Активные кнопки «Купить» и «Купить в кредит»:
#  переключение между кнопками происходит без ошибок. (позитивный сценарий)

import pytest
from page.main_pages import MainPages

def test_active_buttons(driver):
    main_pages = MainPages(driver)
    main_pages.open()
    buy_button = main_pages.find(MainPages.BUY_BUTTON)
    credit_button = main_pages.find(MainPages.CREDIT_BUTTON)
    buy_button.click()
    assert "Успешно" in driver.page_source
    credit_button.click()
    assert "Кредит оформлен" in driver.page_source