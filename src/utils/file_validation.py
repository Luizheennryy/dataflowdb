import csv
from src.config.log import logger

def is_valid_csv(file_path: str) -> bool:
    """
    Retorna True se o CSV existir e tiver mais de uma linha (cabeçalho + pelo menos 1 registro).
    Tenta abrir mesmo que o encoding contenha caracteres inválidos.
    """
    try:
        with open(file_path, "r", encoding="iso-8859-1", errors="ignore") as f:
            reader = csv.reader(f, delimiter=";")
            rows = list(reader)
            if len(rows) <= 1:
                return False
            return True
    except FileNotFoundError:
        logger.warning(f"⚠️ Arquivo não encontrado: `{file_path}`")
        return False
    except Exception as e:
        logger.error(f"❌ Erro ao validar CSV `{file_path}`: {e}")
        return False
