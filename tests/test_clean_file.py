import os
from src.utils.csv_cleaner import clean_csv

def test_clean_file(tmp_path):
    # Cria um CSV temporário com conteúdo sujo
    dirty_content = "nome,idade\nJoão,25\nMaria,30\n'Alfredo',45"
    test_file = tmp_path / "dirty.csv"
    test_file.write_text(dirty_content, encoding="latin1")

    # Executa a limpeza
    clean_csv(str(test_file))

    # Lê novamente o arquivo limpo
    cleaned_content = test_file.read_text(encoding="latin1")

    # Verifica se a limpeza foi feita corretamente
    assert "'" not in cleaned_content
    assert "," not in cleaned_content
    assert ";" in cleaned_content
    assert "João;25" in cleaned_content
