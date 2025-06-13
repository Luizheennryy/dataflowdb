import pytest
from src.pipelines.csv_to_postgres import run_csv_to_postgres
from src.database.connection import get_connection

TEST_TABLE = "test_table"

@pytest.fixture(scope="function")
def connection():
    conn = get_connection()
    yield conn
    conn.rollback()
    conn.close()

def test_copy_csv_to_postgres_success(connection, tmp_path):
    # ⚠️ Limpa a tabela antes de executar o teste
    with connection.cursor() as cur:
        cur.execute(f"TRUNCATE TABLE {TEST_TABLE};")
        connection.commit()

    # Cria um arquivo CSV de teste
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text("id;descricao\n1;Primeiro\n2;Segundo", encoding="latin1")

    # Executa a função de carga
    run_csv_to_postgres(TEST_TABLE, str(csv_file), connection)

    # Valida que 2 registros foram inseridos
    cursor = connection.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {TEST_TABLE}")
    count = cursor.fetchone()[0]
    assert count == 2

    # Verifica os valores da coluna `descricao`
    cursor.execute(f"SELECT descricao FROM {TEST_TABLE} ORDER BY id")
    results = [row[0] for row in cursor.fetchall()]
    assert results == ["Primeiro", "Segundo"]
