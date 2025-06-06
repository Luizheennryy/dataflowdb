import os
from src.database.connection import get_connection
from src.config.log import logger

def preprocess_file(file_path: str, replacements: list[tuple]) -> None:
    with open(file_path, "r", newline="") as file:
        content = file.read()
        for old, new in replacements:
            content = content.replace(old, new)

    with open(file_path, "w", newline="") as file:
        file.write(content)

def load_csv_to_postgres(table: str, file_path: str) -> None:
    conn = get_connection()
    with conn.cursor() as curs:
        with open(file_path, "r") as f:
            copy_sql = f"""
                COPY {table} FROM stdin WITH CSV HEADER
                DELIMITER ';' NULL 'null' QUOTE '"'
            """
            curs.copy_expert(sql=copy_sql, file=f)
            logger.info(f"Tabela `{table}` carregada com sucesso.")

    conn.commit()
    conn.close()

def run_load_pipeline(file_path: str, table: str) -> None:
    logger.info(f"Iniciando pipeline para a tabela: {table}")

    preprocess_file(file_path, [("'", ""), (",", ";")])
    load_csv_to_postgres(table, file_path)

    logger.info(f"Pipeline de carga para `{table}` concluída com sucesso.")