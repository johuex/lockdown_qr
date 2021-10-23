import psycopg2
from psycopg2.extras import DictCursor
from .config import Config


def connect_db():
    """
    Get connection to DB and cursor
    :return: Connection and Cursor
    """
    connection = psycopg2.connect(
                            dbname=Config.DB_DB,
                            user=Config.DB_USER,
                            password=Config.DB_PASS,
                            host=Config.DB_PATH,
                            port=5432
                            )
    cursor = connection.cursor()
    return connection, cursor


def sql_request(sql: str, params: tuple, commit: bool = False, fetch: bool = True):
    """
    Returning result of SQL-request
    :param commit: commit or not commit
    :param fetch: fetch or not fetch
    :param sql: SQL-request in str
    :param params: params in SQL-request in tuple
    :return: result of SQL-request
    """
    conn, curs = connect_db()
    curs.execute(sql, params)
    result = None
    if fetch:
        result = curs.fetchone()
    if commit:
        conn.commit()
    conn.close()
    return result
