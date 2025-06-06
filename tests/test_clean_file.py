from src.utils.csv_cleaner import clean_file

def test_clean_file(tmp_path):
    dirty_content = "nome,idade\nJoão,25\nMaria,30\n'Alfredo',45"
    test_file = tmp_path / "dirty.csv"
    test_file.write_text(dirty_content, encoding="latin1")

    clean_file(str(test_file))

    cleaned_content = test_file.read_text(encoding="latin1")

    assert "'" not in cleaned_content
    assert "," not in cleaned_content
    assert ";" in cleaned_content
    assert "João;25" in cleaned_content
