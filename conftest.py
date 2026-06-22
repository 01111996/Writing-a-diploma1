import pytest
import requests
import time
from utils.bd_utils import check_payment_in_db
from utils.browser import create_driver


@pytest.fixture(scope='session')
def driver():
    a = create_driver()
    yield a
    a.quit()

#Проверка статуса платежа в БД
@pytest.fixture
def assert_db_status_success():
    order_id = yield
    if order_id is None:
        pytest.fail("Не получен order_id для проверки в БД!")
    print(f"Проверка статуса платежа с order_id: {order_id} в БД")
    is_success = check_payment_in_db(order_id)
    assert is_success, f"Статус в БД не'SUCCESS'. Проверьте, что данные корректны."