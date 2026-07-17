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
    'port': os.environ.get('DB_PORT', '3306'),  
}

@contextmanager
def get_db_connection():
    connection = None
    try:
        logger.info(f"Попытка подключения к БД с параметрами: {DB_CONFIG}")
        connection = mysql.connector.connect(**DB_CONFIG)
        yield connection
    except Error as e:
        logger.error(f"Ошибка подключения к MySQL: {e}", exc_info=True)
        raise
    finally:
        if connection and connection.is_connected():
            logger.info("Закрытие соединения с БД")
            connection.close()

#для проверки created
def _get_timestamp_column(conn, table: str) -> str:
    query = """
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = DATABASE()
          AND TABLE_NAME   = %s
          AND COLUMN_NAME IN ('created', 'created_at', 'timestamp', 'create_date')
        LIMIT 1;
    """
    with conn.cursor() as cursor:
        cursor.execute(query, (table,))
        result = cursor.fetchone()
    if result:
        col = result[0]
        logger.info(f"Колонка временной метки в '{table}': '{col}'")
        return col
    logger.warning(f"Колонка временной метки не найдена в '{table}', fallback → 'created'")
    return "created"

def check_payment_in_db(since_ts, expected_status: str, table: str = "payment_entity") -> bool:
    query = f"SELECT status FROM {table} WHERE created >= %s ORDER BY created ASC LIMIT 1;"
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (since_ts,))
                result = cursor.fetchone()
                if result is None:
                    logger.warning(f"В таблице {table} не найдено записей после {since_ts}.")
                    return False
                actual_status = result[0]
                logger.info(f"Найден статус в БД ({table}): {actual_status}, ожидали: {expected_status}")
                return actual_status == expected_status
    except Error as e:
        print(f"Ошибка при выполнении запроса к БД ({table}): {e}")
        return False



