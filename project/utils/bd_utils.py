import mysql.connector
from mysql.connector import Error
import configparser
import os
from contextlib import contextmanager


CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'application.properties')

config = configparser.ConfigParser()
with open(CONFIG_PATH) as f:
    config.read_string("[config]\n" + f.read())

db_url = config.get('config', 'spring.datasource.url')
address_and_db = db_url.replace('jdbc:mysql://', '')
host, database = address_and_db.split('/', 1)
host, port = host.split(':')
DB_CONFIG = {
    'database': database,
    'user': config.get('config', 'spring.datasource.username'),
    'password': config.get('config', 'spring.datasource.password'),
    'host': host,
    'port': port,
}

@contextmanager
def get_db_connection():
    connection = None
    try:
        print(f"Пробую подключиться к БД с параметрами: {DB_CONFIG}")
        connection = mysql.connector.connect(**DB_CONFIG)
        yield connection
    except Error as e:
        print(f"Ошибка при подключении к MySQL: {e}")
        raise 
    finally:
        if connection and connection.is_connected():
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


