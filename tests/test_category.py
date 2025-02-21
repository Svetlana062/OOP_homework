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
        product = Product("Телефон", "Смартфон", 500.0, 10)
        self.category.add_product(product)
        self.assertEqual(len(self.category.get_products), 1)  # Проверяем, что продукт добавлен
        self.assertEqual(
            self.category.get_products[0].name, "Телефон"
        )  # Проверяем, что добавленный продукт правильный

    def test_add_invalid_product(self):
        """Тестируем добавление невалидного продукта."""
        with self.assertRaises(ValueError):
            self.category.add_product("Некорректный продукт")  # Передаем строку вместо объекта Product

    def test_products_property(self):
        """Тестируем свойство products."""
        product1 = Product("Телефон", "Смартфон", 500.0, 10)
        product2 = Product("Ноутбук", "Игровой ноутбук", 1500.0, 5)
        self.category.add_product(product1)
        self.category.add_product(product2)

        expected_output = "Телефон, 500.0 руб. Остаток: 10 шт.\n" "Ноутбук, 1500.0 руб. Остаток: 5 шт."
        self.assertEqual(self.category.products, expected_output)


if __name__ == "__main__":
    unittest.main()
