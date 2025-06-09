import pytest
from src.database.connection import get_connection
from src.database.delete_by_period import delete_by_period

TEST_TABLE = "test_table"

@pytest.fixture(scope="function")
def connection():
    conn = get_connection()
    yield conn
    conn.rollback()
    conn.close()

def test_delete_by_period_removes_correct_rows(connection):
    cursor = connection.cursor()

    # Setup: Insere duas linhas, com períodos diferentes
    cursor.execute(f"INSERT INTO {TEST_TABLE} (id, descricao) VALUES (1, '202401'), (2, '202506')")
    connection.commit()

    # Verifica que os dados foram inseridos
    cursor.execute(f"SELECT COUNT(*) FROM {TEST_TABLE}")
    total_before = cursor.fetchone()[0]
    assert total_before == 2

    # Executa o delete com filtro por periodo
    delete_by_period(connection, TEST_TABLE, "descricao", "202401")

    # Verifica se apenas o valor correspondente foi removido
    cursor.execute(f"SELECT descricao FROM {TEST_TABLE}")
    result = [row[0] for row in cursor.fetchall()]
    
    assert "202401" not in result
    assert "202506" in result
