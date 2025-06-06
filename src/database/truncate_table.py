from src.config.log import logger

def truncate_table(conn, table: str):
    """
    Executa TRUNCATE na tabela especificada.
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"TRUNCATE {table}")
            conn.commit()
            logger.info(f"💨 TRUNCATE executado com sucesso na tabela `{table}`")
    except Exception as e:
        conn.rollback()
        logger.error(f"❌ Erro ao truncar tabela `{table}`: {e}")
        raise
