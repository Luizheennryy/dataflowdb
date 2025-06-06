import pytest
from src.utils.file_validation import is_valid_csv

@pytest.mark.parametrize("content,expected", [
    ("id;name\n1;John\n2;Jane", True),
    ("id;name", False),
    ("", False),
])
def test_is_valid_csv_cases(content, expected, tmp_path):
    test_file = tmp_path / "test.csv"
    test_file.write_text(content, encoding="cp1252")
    assert is_valid_csv(str(test_file)) == expected

def test_is_valid_csv_file_not_found():
    assert is_valid_csv("non_existent_file.csv") is False
