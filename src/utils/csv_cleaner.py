from src.config.log import logger

def clean_file(file_path: str):
    """
    Limpa o arquivo CSV:
    - Remove aspas simples
    - Substitui vírgulas por ponto e vírgula
    - Remove linhas com apenas delimitadores ou vazias
    - Não regrava se não houver necessidade
    """
    try:
        with open(file_path, "r", encoding="iso-8859-1", errors="ignore") as f:
            lines = f.readlines()
    except Exception as e:
        logger.error(f"❌ Erro ao ler `{file_path}` no clean_file: {e}")
        raise

    cleaned_lines = []
    for line in lines:
        cleaned = line.replace("'", "").replace(",", ";").strip()
        if cleaned and not all(c == ";" for c in cleaned):
            cleaned_lines.append(cleaned + "\n")

    # Reescreve o arquivo apenas se houver alteração
    if cleaned_lines and cleaned_lines != lines:
        with open(file_path, "w", encoding="iso-8859-1", errors="ignore") as f:
            f.writelines(cleaned_lines)
