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


class TestCategoryAddition(unittest.TestCase):

    def setUp(self):
        """Создание необходимых для тестов объектов."""
        self.product_a1 = Product(
            name="Смартфон A", description="Описание A", price=50000, quantity=10, color="черный"
        )
        self.product_a2 = Product(name="Смартфон B", description="Описание B", price=60000, quantity=5, color="белый")

        self.category_a = Category(name="Смартфоны", description="Категория смартфонов")
        self.category_b = Category(name="Смартфоны", description="Категория смартфонов")

        # Добавляем продукты в категории
        self.category_a.add_product(self.product_a1)
        self.category_a.add_product(self.product_a2)

        self.product_b1 = Product(
            name="Смартфон C", description="Описание C", price=55000, quantity=3, color="красный"
        )
        self.product_b2 = Product(name="Смартфон D", description="Описание D", price=45000, quantity=2, color="синий")
        self.category_b.add_product(self.product_b1)
        self.category_b.add_product(self.product_b2)

    def test_add_same_type_categories(self):
        """Тест на сложение категорий с одинаковыми продуктами."""
        total_cost = self.category_a + self.category_a
        expected_cost = (50000 * 10 + 60000 * 5) * 2  # Удвоить стоимость
        self.assertEqual(total_cost, expected_cost)

    def test_add_different_type_categories(self):
        """Тест на сложение категорий с разными классами продуктов."""
        with self.assertRaises(TypeError):
            self.category_a + "некорректный тип"

    def test_add_empty_categories(self):
        """Тест на сложение пустых категорий."""
        empty_category_a = Category(name="Пустая категория A", description="Пустая категория")
        empty_category_b = Category(name="Пустая категория B", description="Пустая категория")
        total_cost = empty_category_a + empty_category_b  # Ожидается 0
        self.assertEqual(total_cost, 0)

    def test_add_categories_with_empty_and_non_empty(self):
        """Тест на сложение пустой категории с непустой."""
        empty_category = Category(name="Пустая категория", description="Пустая категория")
        total_cost = self.category_a + empty_category  # Ожидается стоимость из category_a
        expected_cost = 50000 * 10 + 60000 * 5
        self.assertEqual(total_cost, expected_cost)


if __name__ == "__main__":
    unittest.main()
