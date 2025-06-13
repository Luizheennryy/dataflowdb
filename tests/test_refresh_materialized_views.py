import pytest
from src.database.connection import get_connection
from src.pipelines.refresh_views.refresh_materialized_views import refresh_materialized_views

TEST_VIEW = "test_view_mview"

@pytest.fixture(scope="function")
def connection():
    conn = get_connection()
    yield conn
    conn.rollback()
    conn.close()

def test_refresh_materialized_views(connection):
    cursor = connection.cursor()

    # Garante que a view e a tabela não existam antes
    cursor.execute(f"DROP MATERIALIZED VIEW IF EXISTS {TEST_VIEW}")
    cursor.execute("DROP TABLE IF EXISTS test_view_table CASCADE")

    # Cria a tabela e popula
    cursor.execute("CREATE TABLE test_view_table (id SERIAL PRIMARY KEY, valor TEXT)")
    cursor.execute("INSERT INTO test_view_table (valor) VALUES ('primeiro'), ('segundo')")

    # Cria a view materializada
    cursor.execute(f"CREATE MATERIALIZED VIEW {TEST_VIEW} AS SELECT * FROM test_view_table")
    connection.commit()

    # Executa o refresh
    refresh_materialized_views([TEST_VIEW])

    # Valida os dados
    cursor.execute(f"SELECT COUNT(*) FROM {TEST_VIEW}")
    count = cursor.fetchone()[0]
    assert count == 2
