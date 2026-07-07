import os
import sys
from dotenv import load_dotenv
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
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

os.makedirs("logs", exist_ok=True)    

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename=f'logs/test_automation_{datetime.now().strftime("%Y-%m-%d")}.log', 
    filemode='a'
)

@pytest.fixture(scope='function')
def driver():
    driver_instance = create_driver()
    if not driver_instance:
        pytest.exit("Не удалось создать экземпляр WebDriver. Проверьте установку Chrome.", returncode=1)
    logging.info("WebDriver успешно создан.")
    yield driver_instance
    try:
        driver_instance.quit()
        logging.info("WebDriver закрыт.")
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
        nodeid_safe = rep.nodeid.replace('::', '_').replace('/', '__')
        filename = f"screenshot_{timestamp}_{nodeid_safe}.png"
        
        try:
            save_path = os.path.join("project", "tests", "screenshots", filename)
            src_path = save_path.replace(".png", "_pagesource.html")
            with open(src_path, "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            logging.info(f"Page source: {src_path}")
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            
            driver.save_screenshot(save_path)
            print(f"\n===PAGE SOURCE===\n{driver.page_source[:4000]}\n===END===", flush=True)
            logging.info(f"Скриншот падения: {save_path}")

            allure.attach.file(
                source=save_path,
                name="Скриншот ошибки",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            logging.error(f"Ошибка при сохранении скриншота: {e}")


#Проверка статуса платежа в БД
@pytest.fixture
def assert_db_status_success():
    order_id = yield
    if order_id is None:
        pytest.fail("Не получен order_id для проверки в БД.")
        
    print(f"Проверка статуса платежа с order_id: {order_id} в БД.")
    logging.info(f"Проверка заказа {order_id} в БД.")
    
    is_success = check_payment_in_db(order_id)
    assert is_success, f"Статус в БД не 'SUCCESS'. Проверьте данные."


