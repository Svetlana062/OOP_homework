from unittest.mock import patch

import pytest

from src.product import Product


def test_product_init(product_1):
    """Тест класса Products"""
    assert product_1.name == "Смартфоны"
    assert product_1.description == "Описание 1"
    assert product_1.price == 24000
    assert product_1.quantity == 18


def test_create_new_product():
    """Проверяем, что продукт добавлен."""
    product_info = {
        "name": "Холодильник",
        "description": "Описание товара 1",
        "price": 50000.0,
        "quantity": 5,
    }
    product = Product.new_product(product_info)
    assert product.name == "Холодильник"
    assert product.price == 50000.0
    assert product.quantity == 5
    assert len(Product.existing_products) == 1


def test_update_existing_product():
    """Тест на обновление существующего продукта и добавление нового"""
    product_info_1 = {
        "name": "Товар 1",
        "description": "Описание товара 1",
        "price": 100.0,
        "quantity": 5,
    }
    product_info_2 = {
        "name": "Товар 1",
        "description": "Обновленное описание товара 1",
        "price": 120.0,
        "quantity": 10,
    }

    # Создание первого продукта
    product_first = Product.new_product(product_info_1)
    assert product_first.name == "Товар 1"
    assert product_first.price == 100
    assert product_first.quantity == 5

    # Обновление существующего продукта
    product_second = Product.new_product(product_info_2)

    assert product_second.name == "Товар 1"
    assert product_second.price == 120.0  # Проверяем, что цена обновилась
    assert product_second.quantity == 15  # Проверяем, что количество обновилось (5 + 10)


def test_price_setter_confirmation():
    """Проверяем изменение цены."""
    product_info = {
        "name": "Товар 1",
        "description": "Описание товара 1",
        "price": 100.0,
        "quantity": 5,
    }

    product = Product.new_product(product_info)
    previous_price = product.price  # Сохраняем предыдущую цену

    with patch("builtins.input", return_value="y"):  # Имитация выбора 'y' (Yes)
        product.price = 80.0  # Процесс понижения цены
        assert product.price == 80.0  # Цена должна измениться
        assert previous_price == 100.0  # Проверяем, что предыдущая цена была 100.0


def test_price_setter_rejection():
    """Проверяем, что цена не изменяется, если пользователь отказывается."""
    product_info = {
        "name": "Товар 1",
        "description": "Описание товара 1",
        "price": 100.0,
        "quantity": 5,
    }

    product = Product.new_product(product_info)
    previous_price = product.price  # Сохраняем предыдущую цену

    with patch("builtins.input", return_value="n"):  # Имитация выбора 'n' (No)
        product.price = 80.0  # Пытаемся понизить цену
        assert product.price == previous_price  # Цена не должна измениться


def test_price_setter_invalid():
    """Проверяем установку некорректной (отрицательной) цены."""
    product_info = {
        "name": "Товар 1",
        "description": "Описание товара 1",
        "price": 100.0,
        "quantity": 5,
    }

    product = Product.new_product(product_info)

    with patch("builtins.print") as mock_print:
        product.price = -100.0  # Пытаемся установить отрицательную цену
        mock_print.assert_called_with("Цена не должна быть нулевая или отрицательная")


def test_product_str(product_1):
    """Тест строки отображения товара."""
    product = product_1
    assert str(product) == "Смартфоны, 24000 руб. Остаток: 18 шт."


def test_product_addition(product_1):
    """Тест на сложение цен и количеств товаров."""
    another_product = Product("Ноутбук", "Описание 2", 150000, 5)
    total_price = product_1 + another_product
    assert total_price == (product_1.price * product_1.quantity) + (another_product.price * another_product.quantity)


if __name__ == "__main__":
    pytest.main()
