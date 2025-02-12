import os
import unittest
from unittest.mock import mock_open, patch

from src.category import Category
from src.product import Product
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
    def test_read_json_file_not_found(self, mock_file):
        result = read_json("dummy_path.json")
        expected = {}
        self.assertEqual(result, expected)

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"')
    def test_read_json_json_decode_error(self, mock_file):
        result = read_json("dummy_path.json")
        expected = {}
        self.assertEqual(result, expected)


class TestCreateObjectsFromJsonFunction(unittest.TestCase):

    def test_create_objects_from_json(self):
        # Пример входных данных
        data = [
            {
                "name": "Category 1",
                "description": "First category",
                "products": [
                    {"name": "Product 1", "description": "Description 1", "price": 10.0, "quantity": 5},
                    {"name": "Product 2", "description": "Description 2", "price": 20.0, "quantity": 3},
                ],
            },
            {
                "name": "Category 2",
                "description": "Second category",
                "products": [{"name": "Product 3", "description": "Description 3", "price": 30.0, "quantity": 2}],
            },
        ]

        # Вызов функции
        result = create_objects_from_json(data)

        # Проверка результата
        self.assertEqual(len(result), 2)  # Должно быть 2 категории

        # Проверка первой категории
        self.assertIsInstance(result[0], Category)
        self.assertEqual(result[0].name, "Category 1")
        self.assertEqual(result[0].description, "First category")
        self.assertEqual(len(result[0].products), 2)  # Должно быть 2 продукта в первой категории

        # Проверка первого продукта в первой категории
        self.assertIsInstance(result[0].products[0], Product)
        self.assertEqual(result[0].products[0].name, "Product 1")
        self.assertEqual(result[0].products[0].price, 10.0)
        self.assertEqual(result[0].products[0].quantity, 5)

        # Проверка второй категории
        self.assertIsInstance(result[1], Category)
        self.assertEqual(result[1].name, "Category 2")
        self.assertEqual(result[1].description, "Second category")
        self.assertEqual(len(result[1].products), 1)  # Должно быть 1 продукт во второй категории

        # Проверка продукта во второй категории
        self.assertIsInstance(result[1].products[0], Product)
        self.assertEqual(result[1].products[0].name, "Product 3")
        self.assertEqual(result[1].products[0].price, 30.0)
        self.assertEqual(result[1].products[0].quantity, 2)


if __name__ == "__main__":
    unittest.main()
