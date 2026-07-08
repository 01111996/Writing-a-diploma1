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
        screenshots_dir = os.path.join("project", "tests", "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)  
        png_path  = os.path.join(screenshots_dir, f"screenshot_{timestamp}_{nodeid_safe}.png")
        html_path = os.path.join(screenshots_dir, f"pagesource_{timestamp}_{nodeid_safe}.html")
        try:
            page_src = driver.page_source
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(page_src)
            logging.info(f"Page source сохранён: {html_path}")
            driver.save_screenshot(png_path)
            logging.info(f"Скриншот: {png_path}")
            allure.attach.file(
                source=png_path,
                name="Скриншот ошибки",
                attachment_type=allure.attachment_type.PNG
            )
            allure.attach(
                body=page_src.encode("utf-8"),
                name="Page Source",
                attachment_type=allure.attachment_type.HTML
            )
        except Exception as e:
            logging.error(f"Ошибка при сохранении артефактов: {e}")


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


