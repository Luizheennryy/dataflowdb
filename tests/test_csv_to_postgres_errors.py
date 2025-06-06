import os
import pytest
from psycopg2 import errors
from src.pipelines.csv_to_postgres import run_csv_to_postgres
from src.database.connection import get_connection

@pytest.fixture
def connection():
    conn = get_connection()
    yield conn
    conn.rollback()
    conn.close()

def test_csv_with_invalid_format(connection, tmp_path):
    # CSV malformado (faltando delimitadores)
    bad_csv = tmp_path / "bad.csv"
    bad_csv.write_text("id;name\n1Joao\n2;Maria", encoding="cp1252")

    table = "test_table"

    with connection.cursor() as cur:
        cur.execute("""
            CREATE TEMP TABLE test_table (
                id INTEGER,
                name TEXT
            );
        """)
        connection.commit()

    with pytest.raises(Exception):
        run_csv_to_postgres(table, str(bad_csv), connection)

def test_insert_into_nonexistent_table(connection, tmp_path):
    valid_csv = tmp_path / "valid.csv"
    valid_csv.write_text("id;name\n1;Joao\n2;Maria", encoding="cp1252")

    with pytest.raises(errors.UndefinedTable):
        run_csv_to_postgres("nonexistent_table", str(valid_csv), connection)
