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


if __name__ == "__main__":
    pytest.main()
