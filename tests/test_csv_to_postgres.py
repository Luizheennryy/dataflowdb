import os
import pytest
import psycopg2
from src.pipelines.csv_to_postgres import run_csv_to_postgres
from src.database.connection import get_connection

@pytest.fixture
def connection():
    conn = get_connection()
    yield conn
    conn.rollback()
    conn.close()

def test_run_csv_to_postgres_success(connection):
    test_csv_path = os.path.join("tests", "data", "test_valid.csv")
    table = "test_table"

    # Cria a tabela fictícia para o teste
    with connection.cursor() as cur:
        cur.execute(f"""
            CREATE TEMP TABLE {table} (
                id INTEGER,
                name TEXT
            );
        """)
        connection.commit()

    run_csv_to_postgres(table, test_csv_path, connection)

    with connection.cursor() as cur:
        cur.execute(f"SELECT COUNT(*) FROM {table};")
        count = cur.fetchone()[0]
        assert count > 0
