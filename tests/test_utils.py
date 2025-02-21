import os
import unittest
from unittest.mock import mock_open, patch

from src.utils import create_objects_from_json, read_json


class TestReadJsonFunction(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    def test_read_json_success(self, mock_file):
        """Проверка пути к файлу"""
        result = read_json("dummy_path.json")
        expected = {"key": "value"}
        self.assertEqual(result, expected)

        # Получение полного пути для сравнения
        full_path = os.path.abspath("dummy_path.json")
        mock_file.assert_called_once_with(full_path, "r", encoding="UTF-8")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_json_file_not_found(self, mock_data):
        """Тест на обработку отсутствующего файла."""
        result = read_json("dummy_path.json")
        expected = {}
        self.assertEqual(result, expected)

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"')
    def test_read_json_json_decode_error(self, mock_data):
        """new_callable=mock_open создает мок-объект, который имитирует поведение функции open"""
        result = read_json("dummy_path.json")
        expected = {}
        self.assertEqual(result, expected)


def test_read_json_invalid(mock_json_file):
    """Тест на обработку некорректного JSON-файла."""
    with open(mock_json_file, "w", encoding="UTF-8") as f:
        f.write("invalid json")

    data = read_json(mock_json_file)
    assert data == {}  # Проверяем, что возвращается пустой словарь


def test_create_objects_from_json(mock_data):
    """Тест на создание объектов из JSON-данных."""
    categories = create_objects_from_json(mock_data)

    assert len(categories) == 2  # Проверяем, что создано 2 категории
    assert categories[0].name == "Category 1"
    assert categories[0].description == "First category"
    assert len(categories[0].products) == 2  # Проверяем, что в первой категории 2 продукта
    assert categories[0].products[0].name == "Product 1"
    assert categories[0].products[0].price == 10.0

    assert categories[1].name == "Category 2"
    assert categories[1].description == "Second category"
    assert len(categories[1].products) == 1  # Проверяем, что во второй категории 1 продукт
    assert categories[1].products[0].name == "Product 3"
    assert categories[1].products[0].price == 30.0


def test_create_objects_from_json_empty():
    """Тест на создание объектов из пустого JSON-данных."""
    categories = create_objects_from_json([])
    assert categories == []  # Проверяем, что возвращается пустой список


if __name__ == "__main__":
    unittest.main()
