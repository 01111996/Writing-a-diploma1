#Отдельный класс для работы с уведомлениями для error_payment  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NotificationHelper:
    VISIBLE_NOTIFICATION = (By.CSS_SELECTOR, "[class*='notification_visible']")
    FIELD_ERROR = (By.CSS_SELECTOR, "[class*='input__sub']")

    @staticmethod
    def get_notification_text(driver, timeout=50):
        wait = WebDriverWait(driver, timeout)
        notification = wait.until(
            EC.visibility_of_element_located(NotificationHelper.VISIBLE_NOTIFICATION)
        )
        return notification.text.split('\n')[0]

    @staticmethod
    def get_field_error_text(driver, timeout=10):
        wait = WebDriverWait(driver, timeout)
        error = wait.until(
            EC.visibility_of_element_located(NotificationHelper.FIELD_ERROR)
        )
        return error.text