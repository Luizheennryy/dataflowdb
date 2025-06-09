import pytest
from src.database.connection import get_connection
from src.database.truncate_table import truncate_table
from src.config import logger

TEST_TABLE = "test_table"

@pytest.fixture(scope="function")
def connection():
    conn = get_connection()
    yield conn
    conn.rollback()
    conn.close()

def test_truncate_table_removes_all_data(connection):
    cursor = connection.cursor()
    
    # Insere dados temporários
    cursor.execute(f"INSERT INTO {TEST_TABLE} (id, descricao) VALUES (999, 'Teste')")
    
    cursor.execute(f"SELECT COUNT(*) FROM {TEST_TABLE}")
    before = cursor.fetchone()[0]
    assert before > 0

    # Execute o truncate
    truncate_table(connection, TEST_TABLE)
    
    cursor.execute(f"SELECT COUNT(*) FROM {TEST_TABLE}")
    after = cursor.fetchone()[0]
    assert after == 0