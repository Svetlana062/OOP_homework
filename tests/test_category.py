import unittest

import pytest

from src.category import Category
from src.product import Product


class TestCategory(unittest.TestCase):

    def setUp(self):
        """Создаем объект категории перед каждым тестом."""
        self.category = Category(name="Электроника", description="Все о электронике", products=[])

    def test_create_category(self):
        """Тестируем создание категории."""
        self.assertEqual(self.category.name, "Электроника")
        self.assertEqual(self.category.description, "Все о электронике")
        self.assertEqual(self.category.products, "")  # Проверяем, что список продуктов пуст

    def test_add_product(self):
        """Тестируем добавление продукта в категорию."""
        product = Product.new_product(
            {
                "name": "Телефон",
                "description": "Смартфон",
                "price": 500.0,
                "quantity": 10,
            }
        )
        self.category.add_product(product)


def test_add_invalid_product(first_category):
    """Тестируем добавление невалидного продукта."""
    with pytest.raises(ValueError):
        first_category.add_product("Некорректный продукт")  # Передаем строку вместо объекта Product


def test_products_property(category_with_products):
    """Тестируем свойство products."""
    expected_output = "Телефон, 500.0 руб. Остаток: 10 шт.\n" "Ноутбук, 1500.0 руб. Остаток: 5 шт."
    assert category_with_products.products == expected_output


def test_category_init_1(first_category):
    """Тест класса Category"""
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство коммуникации"
    assert first_category.products == (
        "Samsung Galaxy C23, 24000 руб. Остаток: 18 шт.\n"
        "Iphone 16, 90000 руб. Остаток: 13 шт.\n"
        "Xiaomi Redmi Note 11S, 36000 руб. Остаток: 9 шт."
    )
    assert Category.category_count == 5
    assert Category.product_count == 9


def test_category_init_2(second_category):
    """Тест класса Category"""
    assert second_category.name == "Телевизоры"
    assert second_category.description == "Современный телевизор"
    assert second_category.products == (
        '55" QLED 4K, 124000 руб. Остаток: 18 шт.\n'
        "LG 32LM576BPL, 90000 руб. Остаток: 13 шт.\n"
        "Xiaomi TV S Mini LED 55, 36000 руб. Остаток: 9 шт.\n"
        "Philips 4K Ultra HD, 34000 руб. Остаток: 24 шт."
    )
    assert Category.category_count == 6
    assert Category.product_count == 13


if __name__ == "__main__":
    unittest.main()
