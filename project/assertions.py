class Assertions:
    @staticmethod
    def assert_error_notification(actual_result, expected_text='Ошибка'):
        assert expected_text in actual_result, \
            f"Ожидали'{expected_text}', а получили '{actual_result}'"

    @staticmethod
    def assert_declined_notification(actual_result, expected_text='Отклонено'):
        assert expected_text in actual_result, \
            f"Ожидали'{expected_text}', а получили '{actual_result}'"
        
    @staticmethod
    def assert_field_error(actual_result, expected_text='Неверный формат'):
        assert expected_text in actual_result, \
            f"Ожидали '{expected_text}', а получили '{actual_result}'"