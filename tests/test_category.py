import unittest

from src.category import Category
from src.product import Product


class TestCategory(unittest.TestCase):

    def setUp(self):
        """Создаем объект категории перед каждым тестом."""
        self.category = Category(name="Электроника", description="Все о электронике")

    def test_create_category(self):
        """Тестируем создание категории."""
        self.assertEqual(self.category.name, "Электроника")
        self.assertEqual(self.category.description, "Все о электронике")
        self.assertEqual(len(self.category.products), 0)  # Проверяем, что список продуктов пуст

    def test_add_product(self):
        """Тестируем добавление продукта в категорию."""
        product = Product("Телефон", "Смартфон", 500.0, 10, "Серый")
        self.category.add_product(product)
        self.assertEqual(len(self.category.products), 1)  # Проверяем, что продукт добавлен
        self.assertEqual(self.category.products[0].name, "Телефон")  # Проверяем, что добавленный продукт правильный

    def test_add_invalid_product(self):
        """Тестируем добавление невалидного продукта."""
        with self.assertRaises(TypeError):
            self.category.add_product("Некорректный продукт")  # Передаем строку вместо объекта Product

    def test_products_info(self):
        """Тестируем метод products_info."""
        product1 = Product("Телефон", "Смартфон", 500.0, 10, "Серый")
        product2 = Product("Ноутбук", "Игровой ноутбук", 1500.0, 5, "Черный")
        self.category.add_product(product1)
        self.category.add_product(product2)

        expected_output = "Телефон, 500.0 руб. Остаток: 10 шт.\n" "Ноутбук, 1500.0 руб. Остаток: 5 шт."
        self.assertEqual(self.category.products_info(), expected_output)

    def test_category_str(self):
        """Тестируем строковое представление категории."""
        expected_str = "Электроника, количество продуктов: 0 шт."
        self.assertEqual(str(self.category), expected_str)

    def test_category_iter(self):
        """Тестируем итерацию по продуктам категории."""
        product1 = Product("Телефон", "Смартфон", 500.0, 10, "Серый")
        product2 = Product("Ноутбук", "Игровой ноутбук", 1500.0, 5, "Черный")
        self.category.add_product(product1)
        self.category.add_product(product2)

        products = [product for product in self.category]
        self.assertEqual(len(products), 2)  # Должно быть 2 продукта
        self.assertIn(product1, products)  # Телефон должен быть в списке
        self.assertIn(product2, products)  # Ноутбук должен быть в списке


if __name__ == "__main__":
    unittest.main()
