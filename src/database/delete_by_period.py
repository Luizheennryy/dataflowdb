from src.config.log import logger

def delete_by_period(conn, table_name: str, period_field: str, period_value: str):
    """
    Executa DELETE na tabela filtrando pelo campo de período (period_field = period_value).
    """
    try:
        with conn.cursor() as cursor:
            query = f"DELETE FROM {table_name} WHERE substr({period_field}, 7, 4) || substr({period_field}, 4, 2)  = %s"
            cursor.execute(query, (period_value,))
            conn.commit()
            logger.info(f"✅ Registros deletados de `{table_name}` onde `{period_field}` = {period_value}")
    except Exception as e:
        conn.rollback()
        logger.error(f"❌ Erro ao executar DELETE na tabela `{table_name}`: {e}")
        raise
