from src.config.log import logger

def refresh_materialized_views(conn):
    """
    Atualiza views materializadas pré-definidas.
    """
    views = [
        # "Fato_Analiticos",
        # "Fato_UP",
        # adicionar outras views aqui, se houver
    ]

    try:
        cursor = conn.cursor()
        for view in views:
            logger.info(f"🔄 Atualizando view materializada `{view}`...")
            cursor.execute(f'REFRESH MATERIALIZED VIEW "{view}";')
            logger.info(f"✅ View `{view}` atualizada com sucesso.")
        conn.commit()
        cursor.close()
    except Exception as e:
        conn.rollback()
        logger.error(f"❌ Erro ao atualizar views materializadas: {e}")
        raise
