import os
import unittest
from unittest.mock import mock_open, patch

from src.utils import read_json


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
        """При попытке открыть файл будет вызвано исключение FileNotFoundError"""
        result = read_json("dummy_path.json")
        expected = {}
        self.assertEqual(result, expected)

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"')
    def test_read_json_json_decode_error(self, mock_data):
        """new_callable=mock_open создает мок-объект, который имитирует поведение функции open"""
        result = read_json("dummy_path.json")
        expected = {}
        self.assertEqual(result, expected)


# def test_create_objects_from_json(mock_data):
#     """Тест, который проверяет, как функция create_objects_from_json обрабатывает данные, переданные в виде JSON"""
#     result = create_objects_from_json(mock_data)  # Вызов функции
#
#     # Проверка результата
#     assert len(result) == 2  # Должно быть 2 категории
#
#     # Проверка первой категории
#     assert isinstance(result[0], Category)
#     assert result[0].name == "Category 1"
#     assert result[0].description == "First category"
#     assert len(result[0].products) == 2  # Должно быть 2 продукта в первой категории
#
#     # Проверка первого продукта в первой категории
#     assert isinstance(result[0].products[0], Product)
#     assert result[0].products[0].name == "Product 1"
#     assert result[0].products[0].price == 10.0
#     assert result[0].products[0].quantity == 5
#
#     # Проверка второй категории
#     assert isinstance(result[1], Category)
#     assert result[1].name == "Category 2"
#     assert result[1].description == "Second category"
#     assert len(result[1].products) == 1  # Должно быть 1 продукт во второй категории
#
#     # Проверка продукта во второй категории
#     assert isinstance(result[1].products[0], Product)
#     assert result[1].products[0].name == "Product 3"
#     assert result[1].products[0].price == 30.0
#     assert result[1].products[0].quantity == 2


if __name__ == "__main__":
    unittest.main()
