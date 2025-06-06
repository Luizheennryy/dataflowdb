# import pytest
# from src.database.connection import get_connection
# from tests.delete import truncate_table

# @pytest.fixture
# def connection():
#     conn = get_connection()
#     yield conn
#     conn.rollback()
#     conn.close()

# def test_truncate_table_removes_all_data(connection):
#     table = "temp_truncate_test"

#     with connection.cursor() as cur:
#         cur.execute(f"""
#             CREATE TEMP TABLE {table} (
#                 id SERIAL PRIMARY KEY,
#                 name TEXT
#             );
#         """)
#         cur.execute(f"""
#             INSERT INTO {table} (name) VALUES
#             ('Item 1'),
#             ('Item 2'),
#             ('Item 3');
#         """)
#         connection.commit()

#     # Garante que existem 3 registros antes do truncate
#     with connection.cursor() as cur:
#         cur.execute(f"SELECT COUNT(*) FROM {table};")
#         count_before = cur.fetchone()[0]

#     assert count_before == 3

#     # Executa o TRUNCATE
#     truncate_table(connection, table)

#     # Verifica que todos os dados foram removidos
#     with connection.cursor() as cur:
#         cur.execute(f"SELECT COUNT(*) FROM {table};")
#         count_after = cur.fetchone()[0]

#     assert count_after == 0
