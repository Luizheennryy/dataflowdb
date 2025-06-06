import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = "pipeline_logger", log_file: str = "pipeline.log") -> logging.Logger:
    """
    Cria (ou retorna) um logger único que escreve tanto no console quanto em um arquivo rotacionado em /logs/pipeline.log.
    """
    # Diretório absoluto para a pasta 'logs' (duas pastas acima de config/)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.abspath(os.path.join(base_dir, "..", "..", "logs"))
    os.makedirs(log_dir, exist_ok=True)

    full_log_path = os.path.join(log_dir, log_file)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Se já houver handlers configurados, não adiciona novamente (evita duplicação)
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Handler que imprime no terminal
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        # Handler que escreve em arquivo com rotação
        file_handler = RotatingFileHandler(
            full_log_path, maxBytes=2_000_000, backupCount=5, encoding="utf-8"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

    return logger
