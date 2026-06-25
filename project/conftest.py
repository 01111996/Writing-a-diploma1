import pytest
import requests
import time
import logging
from utils.bd_utils import check_payment_in_db
from utils.browser import create_driver
from datetime import datetime

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='test_automation.log', 
    filemode='a'
)

@pytest.fixture(scope='session')
def driver():
    a = create_driver()
    yield a
    a.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"screenshot_{timestamp}_{rep.nodeid.replace('::', '_')}.png"
            driver.save_screenshot(filename)
            allure.attach.file(filename, name="screenshot", attachment_type=allure.attachment_type.PNG)

#Проверка статуса платежа в БД
@pytest.fixture
def assert_db_status_success():
    order_id = yield
    if order_id is None:
        pytest.fail("Не получен order_id для проверки в БД!")
    print(f"Проверка статуса платежа с order_id: {order_id} в БД")
    is_success = check_payment_in_db(order_id)
    assert is_success, f"Статус в БД не'SUCCESS'. Проверьте, что данные корректны."

#Не прошла оплата по карте
@pytest.fixture(scope="function")
def payment_page(driver):
    main_page = MainPage(driver)
    payment_page = PaymentPage(driver)
    main_page.open()
    main_page.click_buy() 
    return payment_page 