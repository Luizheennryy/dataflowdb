from io import StringIO
from src.config.log import logger
from src.utils.file_helpers import detect_encoding, get_clean_lines

def run_csv_to_postgres(table_name: str, file_path: str, conn):
    try:
        encoding = detect_encoding(file_path)
        logger.info(f"🧠 Encoding detectado: {encoding}")

        cleaned_lines = get_clean_lines(file_path, encoding)
        stream = StringIO("".join(cleaned_lines))

        with conn.cursor() as cur:
            logger.info(f"📥 Iniciando carga para `{table_name}`")
            cur.copy_expert(
                f"COPY {table_name} FROM STDIN WITH CSV HEADER DELIMITER ';';",
                stream
            )
        conn.commit()
        logger.info(f"✅ Carga finalizada para `{table_name}`")

    except Exception as e:
        conn.rollback()
        logger.error(f"❌ Erro durante a carga de `{table_name}`: {e}")
        raise
