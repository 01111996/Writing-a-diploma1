#Отдельный класс для работы с уведомлениями для error_payment  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NotificationHelper:
    VISIBLE_NOTIFICATION = (By.CSS_SELECTOR, "[class*='notification_visible']")
    @staticmethod
    def get_notification_text(driver, timeout=15):
        wait = WebDriverWait(driver, timeout)
        notification = wait.until(
            EC.visibility_of_element_located(NotificationHelper.VISIBLE_NOTIFICATION)
        )
        return notification.text.split('\n')[0]    