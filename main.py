import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.config.log                                             import logger
from src.database.connection                                    import get_connection
from src.database.truncate_table                                import truncate_table
from src.database.delete_by_period                              import delete_by_period
from src.pipelines.refresh_views.refresh_materialized_views     import refresh_materialized_views
from src.pipelines.csv_to_postgres                              import run_csv_to_postgres
from src.utils.file_validation                                  import is_valid_csv

BASE_DIR = os.path.join(os.path.expanduser("~"), "Desktop", "Bases")

delete_date = "202505"

truncate_config = {
    # "dim_capilaridade": "Dim_Capilaridade.csv",
    # "dim_logins_net": "Dim_Logins_Net.csv",
    # "dim_servicos": "Dim_Servicos.csv"
}

table_config = {
    "fato_ur": ("fato_ur.csv", "data", delete_date)
}

def main():
    logger.info("🚀Starting the CSV file ingestion pipeline for PostgreSQL")
    
    conn = None
    try:
        conn = get_connection()
        
        # 1) Complete TRUNCATE on tables that require it
        for table, filename in truncate_config.items():
            file_path = os.path.join(BASE_DIR, filename)
            if not is_valid_csv(file_path):
                logger.warning(f"⚠️ File `{filename}` invalid or empty. Ignored `{table}`.")
                continue
            
            logger.info(f"📄 Table load `{table}` by truncating with `{filename}`.")
            try:
                truncate_table(conn, table)
                run_csv_to_postgres(table, file_path, conn)
                logger.info(f"✅ Load completed for `{table}` (TRUNCATE).")
            except Exception as e:
                logger.error(f"❌ Error in `{table}` (TRUNCATE): {e}.")

        # 2) DELETE for period + INSERT for other facts
        for table, (filename, filter_column, filter_value) in table_config.items():
            file_path = os.path.join(BASE_DIR, filename)
            if not is_valid_csv(file_path):
                logger.warning((f"⚠️ File `{filename}` invalid or empty. Ignored `{table}`.")) 
                continue
            
            logger.info(f"📄 Table load `{table}` by truncating with `{filename}`.")
            try:
                delete_by_period(conn, table, filter_column, filter_value)
                run_csv_to_postgres(table, file_path, conn)
                logger.info(f"✅ Load completed for `{table}` (TRUNCATE).")
            except Exception as e:
                logger.error(f"❌ Error in `{table}` (TRUNCATE): {e}.")
                
        # 3) RefreshRefresh materialized views
        try:
            refresh_materialized_views(conn)
        except Exception as e:
            logger.error(f"❌ Error refreshing materialized views: {e}.")
    
    except Exception as e:
        logger.error(f"❌ Error connecting to database: {e}.")
        
    finally:
        if conn:
            conn.close()
            logger.info("🔒 PostgreSQL connection closed." )
            
if __name__ == "__main__":
    main()
