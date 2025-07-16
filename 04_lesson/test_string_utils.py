import pytest
import unittest
from string_utils import StringUtils

string_utils = StringUtils()

# Положительные тесты для capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("123abc", "123abc"),  # Числа не меняются
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Отрицательные тесты для capitalize
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),              # Пустая строка
    ("   ", "   "),        # Пробелы не изменяются
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Положительные тесты для trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("  hello world", "hello world"),
    ("   python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

# Отрицательные тесты для trim
@pytest.mark.negative
@pytest.mark.parametrize("input_str", [
    123,               # Число не строка
    None,              # None не строка
    3.14,              # Число с плавающей запятой не строка
])
def test_trim_negative(input_str):
    with pytest.raises(TypeError):
        string_utils.trim(input_str)

# Положительные тесты для contains:
def test_contains_symbol_found_start():
    # Символ "S" есть в начале строки "SkyPro"
    utils = StringUtils()
    assert utils.contains("SkyPro", "S") == True

def test_contains_symbol_found_middle():
    # Символ "o" есть в середине строки "Hello, World!"
    utils = StringUtils()
    assert utils.contains("Hello, World!", "o") == True

# Негативные тесты для contains:
def test_contains_symbol_not_found():
    # Символ "x" отсутствует в строке "SkyPro"
    utils = StringUtils()
    assert utils.contains("SkyPro", "x") == False

def test_contains_symbol_in_empty_string():
    # Любой символ отсутствует в пустой строке
    utils = StringUtils()
    assert utils.contains("", "a") == False

# Положительные тесты для delete_symbol:
def test_delete_existing_symbol():
    # Удаляем символ "k" из "SkyPro"
    utils = StringUtils()
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_existing_substring():
    # Удаляем подстроку "Pro" из "SkyPro"
    utils = StringUtils()
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

# Негативные тесты для delete_symbol:
def test_delete_non_existing_symbol():
    # Пытаемся удалить "x", которого нет в строке
    utils = StringUtils()
    assert utils.delete_symbol("SkyPro", "x") == "SkyPro"

def test_delete_from_empty_string():
    # Пытаемся удалить "a" из пустой строки
    utils = StringUtils()
    assert utils.delete_symbol("", "a") == ""