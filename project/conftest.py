import os
from dotenv import load_dotenv
import sys
sys.path.insert(0, '.')
import allure
import pytest
import requests
import time
import logging
from project.utils.bd_utils import check_payment_in_db
from project.utils.browser import create_driver
from datetime import datetime

load_dotenv()
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir) 
sys.path.append(parent_dir)

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='test_automation.log', 
    filemode='a'
)

@pytest.fixture(scope='session')
def driver():
    driver_instance = create_driver()
    if not driver_instance:
        pytest.exit("Не удалось создать экземпляр WebDriver. Проверьте установку Chrome.", returncode=1)
    yield driver_instance
    try:
        driver_instance.quit()
    except Exception as e:
        logging.error(f"Ошибка при закрытии драйвера: {e}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver is None:
            logging.error("Проверьте фикстуры.")
            return
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{timestamp}_{rep.nodeid.replace('::', '_')}.png"
        try:
            driver.save_screenshot(filename)
            allure.attach.file(filename, ..., attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            logging.error(f"Ошибка при сохранении скриншота: {e}")

#Проверка статуса платежа в БД
@pytest.fixture
def assert_db_status_success():
    order_id = yield
    if order_id is None:
        pytest.fail("Не получен order_id для проверки в БД!")
    print(f"Проверка статуса платежа с order_id: {order_id} в БД")
    is_success = check_payment_in_db(order_id)
    assert is_success, f"Статус в БД не'SUCCESS'. Проверьте, что данные корректны."


