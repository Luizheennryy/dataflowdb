from src.database.connection import get_connection
from src.config.log import logger

def refresh_materialized_views(views: list[str]):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            for view in views:
                logger.info(f"🔄 Atualizando view materializada: {view}")
                cur.execute(f"REFRESH MATERIALIZED VIEW {view};")
        conn.commit()
        logger.info("✅ Views atualizadas com sucesso!")
    except Exception as e:
        conn.rollback()
        logger.error(f"❌ Erro ao atualizar views: {e}")
        raise
    finally:
        conn.close()
