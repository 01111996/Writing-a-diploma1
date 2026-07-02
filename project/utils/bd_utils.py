import mysql.connector
from mysql.connector import Error
import os
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)

DB_CONFIG = {
    'database': os.environ.get('DB_NAME'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': os.environ.get('DB_HOST'),
    'port': os.environ.get('DB_PORT', '3306'),  # 3306 — порт по умолчанию, если не задан
}

@contextmanager
def get_db_connection():
    connection = None
    try:
        logger.info(f"Пробую подключиться к БД с параметрами: {DB_CONFIG}")
        connection = mysql.connector.connect(**DB_CONFIG)
        yield connection
    except Error as e:
        logger.error(f"Ошибка при подключении к MySQL: {e}", exc_info=True)
        raise
    finally:
        if connection and connection.is_connected():
            logger.info("Закрываю соединение с БД")
            connection.close()
        
def check_payment_in_db(order_id: str) -> bool:
    query = "SELECT status FROM payments WHERE order_id = %s;"
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (order_id,))
                result = cursor.fetchone()
                return result is not None and result[0] == 'SUCCESS'
    except Error as e:
        print(f"Ошибка при выполнении запроса к БД: {e}")
        return False


