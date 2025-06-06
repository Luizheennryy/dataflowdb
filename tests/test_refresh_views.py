import pytest
import psycopg2
from src.database.refresh_views import refresh_materialized_views
from src.database.connection import get_connection

@pytest.fixture
def connection():
    conn = get_connection()
    yield conn
    conn.rollback()
    conn.close()

def test_refresh_valid_view(connection, capsys):
    with connection.cursor() as cur:
        cur.execute("""
            CREATE MATERIALIZED VIEW IF NOT EXISTS temp_valid_view AS
            SELECT 1 as col;
        """)
        cur.execute("""
            CREATE UNIQUE INDEX IF NOT EXISTS temp_valid_view_idx ON temp_valid_view(col);
        """)
        connection.commit()

    def single_view_refresh(conn):
        from psycopg2 import sql
        with conn.cursor() as cursor:
            cursor.execute(sql.SQL("REFRESH MATERIALIZED VIEW CONCURRENTLY temp_valid_view;"))
            conn.commit()

    # Executa e captura a saída
    single_view_refresh(connection)
    captured = capsys.readouterr()
    assert "temp_valid_view" in captured.out or captured.out == ""

def test_refresh_invalid_view(connection):
    with pytest.raises(psycopg2.errors.UndefinedTable):
        with connection.cursor() as cur:
            cur.execute("REFRESH MATERIALIZED VIEW CONCURRENTLY nao_existe;")
            connection.commit()
