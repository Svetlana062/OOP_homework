import sys
import unittest
from io import StringIO
from unittest.mock import patch

import pytest

from src.base_product import BaseProduct
from src.lawn_grass import LawnGrass
from src.mixin_product import MixinProduct
from src.product import Product
from src.smartphone import Smartphone


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
        "color": "Синий",
    }
    product = Product.new_product(product_info)
    assert product.name == "Холодильник"
    assert product.description == "Описание товара 1"
    assert product.price == 50000.0
    assert product.quantity == 5
    assert product.color == "Синий"
    assert len(Product.existing_products) == 1


def test_update_existing_product():
    """Тест на обновление существующего продукта и добавление нового"""
    product_info_1 = {
        "name": "Товар 1",
        "description": "Описание товара 1",
        "price": 100.0,
        "quantity": 5,
        "color": "Красный",
    }
    product_info_2 = {
        "name": "Товар 1",
        "description": "Обновленное описание товара 1",
        "price": 120.0,
        "quantity": 10,
        "color": "Белый",
    }

    # Создание первого продукта
    product_first = Product.new_product(product_info_1)
    assert product_first.name == "Товар 1"
    assert product_first.description == "Описание товара 1"
    assert product_first.price == 100
    assert product_first.quantity == 5
    assert product_first.color == "Красный"

    # Обновление существующего продукта
    product_second = Product.new_product(product_info_2)

    assert product_second.name == "Товар 1"
    assert product_second.price == 120.0  # Проверяем, что цена обновилась
    assert product_first.description == "Описание товара 1"
    assert product_second.quantity == 15  # Проверяем, что количество обновилось (5 + 10)
    assert product_first.color == "Белый"


def test_price_setter_confirmation():
    """Проверяем изменение цены."""
    product_info = {
        "name": "Товар 1",
        "description": "Описание товара 1",
        "price": 100.0,
        "quantity": 5,
        "color": "Белый",
    }

    product = Product.new_product(product_info)
    previous_price = product.price  # Сохраняем предыдущую цену

    with patch("builtins.input", return_value="y"):  # Имитация выбора 'y' (Yes)
        product.price = 80.0  # Процесс понижения цены
        assert product.price == 80.0  # Цена должна измениться
        assert previous_price == 100.0  # Проверяем, что предыдущая цена была 100.0
        assert product.color == "Белый"


def test_price_setter_rejection():
    """Проверяем, что цена не изменяется, если пользователь отказывается."""
    product_info = {
        "name": "Товар 1",
        "description": "Описание товара 1",
        "price": 100.0,
        "quantity": 5,
        "color": "Белый",
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
        "color": "Белый",
    }

    product = Product.new_product(product_info)

    with patch("builtins.print") as mock_print:
        product.price = -100.0  # Пытаемся установить отрицательную цену
        mock_print.assert_called_with("Цена не должна быть нулевая или отрицательная")


def test_product_str(product_1):
    """Тест строки отображения товара."""
    product = product_1
    assert str(product) == "Смартфоны, 24000 руб. Остаток: 18 шт. Цвет: Синий"


def test_product_addition(product_1):
    """Тест сложения продуктов."""
    other_product = Product(
        name="Другой продукт", description="Описание другого продукта", price=1500, quantity=3, color="Зеленый"
    )
    total_price = product_1 + other_product
    assert total_price == (24000 * 18) + (1500 * 3)


def test_product_addition_with_different_types():
    """Тест сложения продуктов разных типов должен выбросить ошибку TypeError."""

    # Создаем продукты разных типов с требуемыми аргументами
    electronic_product = Smartphone(
        name="Смартфон",  # Название
        description="Современный смартфон",  # Описание
        price=25000,  # Цена
        quantity=10,  # Количество
        efficiency=95.0,  # Производительность
        model="Модель X",  # Модель
        memory=128,  # Объем памяти
        color="черный",  # Цвет
    )

    plant_product = LawnGrass(
        name="Газонная трава",  # Название
        description="Трава для сада",  # Описание
        price=200,  # Цена
        quantity=5,  # Количество
        country="Россия",  # Страна производитель
        germination_period="14 дней",  # Срок прорастания
        color="зеленый",  # Цвет
    )

    # Проверяем, что сложение выбрасывает TypeError
    with pytest.raises(TypeError):
        _ = electronic_product + plant_product  # Мы ожидаем исключение, поэтому не сохраняем значение


# Тесты для класса MixinProduct
def test_mixin_product_initialization(mixin_product):
    """Тест инициализации MixinProduct."""
    assert mixin_product.name == "Миксер"
    assert mixin_product.description == "Описание миксера"
    assert mixin_product.price == 3000
    assert mixin_product.quantity == 10
    assert mixin_product.color == "Красный"


def test_mixin_product_str(mixin_product):
    """Тест строкового представления MixinProduct."""
    assert str(mixin_product) == "Миксер, 3000 руб. Остаток: 10 шт. Цвет: Красный"


def test_mixin_print_output(mixin_product):
    """Тест для проверки вывода информации о создании объекта."""
    captured_output = StringIO()
    sys.stdout = captured_output

    Product("Блендер", "Описание блендера", 5000, 5, "Синий")

    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    assert "Product(Блендер, Описание блендера, 5000, 5)" in output
    assert "Миксер" not in output


def test_product_repr(mixin_product):
    """Тест для проверки корректности представления объекта."""
    assert repr(mixin_product) == "Product(Миксер, Описание миксера, 3000, 10)"


class TestProduct(unittest.TestCase):

    def test_product_is_subclass_of_base_product(self):
        """Проверка, что Product является подклассом BaseProduct."""
        self.assertTrue(issubclass(Product, BaseProduct))

    def test_product_is_subclass_of_mixin_product(self):
        """Проверка, что Product является подклассом MixinProduct."""
        self.assertTrue(issubclass(Product, MixinProduct))

    def test_initialization_with_zero_quantity(self):
        """Тест на то, если пользователь попытается создать экземпляр класса Product с нулевым или
        отрицательным количеством"""
        with self.assertRaises(ValueError) as context:
            Product("Товар", "Описание товара", 100.0, 0, "Красный")
        self.assertEqual(str(context.exception), "Товар с нулевым количеством не может быть добавлен")


if __name__ == "__main__":
    pytest.main()
