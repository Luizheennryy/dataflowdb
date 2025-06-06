# import pytest
# from src.database.delete_by_period import delete_by_period
# from src.database.connection import get_connection

# @pytest.fixture
# def connection():
#     conn = get_connection()
#     yield conn
#     conn.rollback()
#     conn.close()

# def test_delete_by_period_removes_correct_rows(connection):
#     table_name = "test_delete_table"
#     column = "ano_mes"
#     delete_value = "202505"

#     # Cria tabela temporária e insere dados
#     with connection.cursor() as cur:
#         cur.execute(f"""
#             CREATE TEMP TABLE {table_name} (
#                 id SERIAL PRIMARY KEY,
#                 nome TEXT,
#                 {column} TEXT
#             );
#         """)
#         cur.execute(f"""
#             INSERT INTO {table_name} (nome, {column}) VALUES
#             ('João', '202505'),
#             ('Maria', '202504');
#         """)
#         connection.commit()

#     # Executa a função de delete
#     delete_by_period(connection, table_name, column, delete_value)

#     # Verifica se só resta o valor 202504
#     with connection.cursor() as cur:
#         cur.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {column} = %s", (delete_value,))
#         remaining = cur.fetchone()[0]

#     assert remaining == 0
