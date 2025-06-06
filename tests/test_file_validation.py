import os
import pytest
from src.utils.file_validation import is_valid_csv

TEST_DIR = "tests/data"

@pytest.mark.parametrize("filename,content,expected", [
    ("valid.csv", "id;name\n1;John\n2;Jane", True),
    ("header_only.csv", "id;name", False),
    ("empty.csv", "", False),
])
def test_is_valid_csv_cases(filename, content, expected):
    file_path = os.path.join(TEST_DIR, filename)

    # Garante que a pasta de teste exista
    os.makedirs(TEST_DIR, exist_ok=True)

    # Cria o arquivo de teste
    with open(file_path, "w", encoding="cp1252") as f:
        f.write(content)

    # Executa e valida o teste
    assert is_valid_csv(file_path) == expected

    # Limpa o arquivo
    os.remove(file_path)

def test_is_valid_csv_file_not_found():
    file_path = os.path.join(TEST_DIR, "non_existent.csv")
    assert is_valid_csv(file_path) == False
