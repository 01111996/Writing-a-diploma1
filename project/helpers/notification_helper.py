#Отдельный класс для работы с уведомлениями для error_payment
class NotificationHelper:
    @staticmethod
    def get_notification_text(driver):
        notification = driver.switch_to.notification
        return notification.text.split('\n')[0]