Для выполнения автотестов необходимо:
1. Подготовка окружения.
Python 3.12
Создать виртуальное окружение python -m venv venv и .\venv\Scripts\activate . Установить зависимость pip install -r requirements.txt
2. Запуск приложения
Установить Docker Desktop https://docs.docker.com/desktop/release-notes/ (необходимо проверить, чтобы компьютер поддерживал данную программу). В терминае выполнить команду для запуска контейнеров docker-compose up -d
3. Заупск тестов (только после активации виртуальной среды)
Для запуска тестов в терминале выполнить команду pytest --alluredir=allure-results
4. Отчёт о тестировании
Для создания отчёта выполнить команду allure serve allure-results
