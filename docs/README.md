Для выполнения автотестов необходимо:
1. Подготовка окружения.
Установить Python 3.10 https://www.python.org/downloads/
Для запуска кода можно установить редактор кода, например VSC https://code.visualstudio.com/ или воспользоваться терминалом (cmd, PowerShell) на компьютере.
В терминале, в корневой папке cоздать виртуальное окружение Windows: python -m venv venv или macOS/Linux: python3 -m venv venv и Windows: .\venv\Scripts\activate или macOS/Linux: source venv/bin/activate. 
Установить зависимости pip install -r requirements.txt
2. Запуск приложения
Установить Docker Desktop https://docs.docker.com/desktop/release-notes/ (перед установкой необходимо проверить, чтобы компьютер поддерживал данную программу). После установки запустить приложение и в терминале выполнить команду для запуска контейнеров docker-compose up -d и проверить статус docker compose ps
3. Заупск тестов (только после активации виртуальной среды)
Необходимо убедиться, что виртуальное окружение активировано, должно быть указано "(venv)"
Для запуска тестов в терминале выполнить команду pytest --alluredir=allure-results
4. Отчёт о тестировании
Для создания HTML - отчёта выполнить команду allure serve allure-results