import os
import psycopg2
from dotenv import load_dotenv
from src.config.log import logger

load_dotenv()

def get_connection():
    """
    Abre uma conexão com o PostgreSQL usando variáveis definidas em .env:
      HOST, PORT, USER, PASSWD, DATABASE.
    """
    host = os.getenv("HOST")
    port = int(os.getenv("PORT"))
    user = os.getenv("USER")
    passwd = os.getenv("PASSWD")
    database = os.getenv("DATABASE")

    if not all([host, port, user, passwd, database]):
        missing = [v for v in ["HOST", "PORT", "USER", "PASSWD", "DATABASE"] if not os.getenv(v)]
        raise EnvironmentError(f"Variáveis de ambiente faltando: {', '.join(missing)}")

    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=passwd,
            database=database
        )
        logger.info("🔌 Conexão com PostgreSQL estabelecida com sucesso.")
        return conn
    except Exception as e:
        logger.error(f"❌ Falha ao conectar no PostgreSQL: {e}")
        raise
