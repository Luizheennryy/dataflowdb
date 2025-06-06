# src/database/delete.py

import logging

logger = logging.getLogger(__name__)

def delete_by_period(conn, table: str, column: str, value: str):
    with conn.cursor() as cur:
        sql = f"DELETE FROM {table} WHERE {column} = %s"
        cur.execute(sql, (value,))
        conn.commit()

def truncate_table(conn, table: str):
    with conn.cursor() as cur:
        sql = f"TRUNCATE TABLE {table}"
        cur.execute(sql)
        conn.commit()
