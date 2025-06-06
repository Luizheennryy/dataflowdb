import pytest
from src.database.connection import get_connection
from tests.delete import delete_by_period

@pytest.fixture
def connection():
    conn = get_connection()
    yield conn
    conn.rollback()  # Garante que alterações feitas no teste não persistam
    conn.close()

def test_delete_by_period_removes_rows(connection):
    table = "temp_delete_test"
    column = "ano_mes"
    delete_value = "2025-05"

    # Cria tabela temporária e insere dados
    with connection.cursor() as cur:
        cur.execute(f"""
            CREATE TEMP TABLE {table} (
                id SERIAL PRIMARY KEY,
                name TEXT,
                {column} TEXT
            );
        """)
        cur.execute(f"""
            INSERT INTO {table} (name, {column}) VALUES
            ('Registro A', %s),
            ('Registro B', %s),
            ('Registro C', '2024-12');
        """, (delete_value, delete_value))
        connection.commit()

    # Verifica que existem 2 registros com o valor alvo
    with connection.cursor() as cur:
        cur.execute(f"SELECT COUNT(*) FROM {table} WHERE {column} = %s", (delete_value,))
        count_before = cur.fetchone()[0]

    assert count_before == 2

    # Executa o delete
    delete_by_period(connection, table, column, delete_value)

    # Verifica que os registros foram removidos
    with connection.cursor() as cur:
        cur.execute(f"SELECT COUNT(*) FROM {table} WHERE {column} = %s", (delete_value,))
        count_after = cur.fetchone()[0]

    assert count_after == 0
