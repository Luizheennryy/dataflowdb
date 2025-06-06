import chardet

def detect_encoding(file_path: str) -> str:
    with open(file_path, "rb") as f:
        return chardet.detect(f.read(10000))["encoding"]


def get_clean_lines(file_path: str, encoding: str) -> list[str]:
    """
    Retorna as linhas do CSV limpas, sem modificar o arquivo original.
    - Remove aspas simples
    - Substitui vírgulas por ponto e vírgula
    - Remove linhas em branco
    """
    with open(file_path, "r", encoding=encoding, errors="ignore") as f:
        return [
            line.replace("'", "").replace(",", ";")
            for line in f
            if line.strip() != ""
        ]
