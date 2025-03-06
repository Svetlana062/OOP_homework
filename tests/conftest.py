import json

import pytest

from src.category import Category
from src.order import Order
from src.product import Product


@pytest.fixture
def product_1():
    """Фикстура для теста класса Products."""
    return Product("Смартфоны", "Описание 1", 24000, 18, "Синий")


@pytest.fixture(autouse=True)
def clear_existing_products():
    """Этот фикстура будет очищать существующие продукты перед каждым тестом."""
    Product.existing_products.clear()


@pytest.fixture
def mock_json_file(tmp_path, mock_data):
    """Фикстура для создания временного JSON-файла с тестовыми данными."""
    json_file = tmp_path / "test_data.json"
    with open(json_file, "w", encoding="UTF-8") as f:
        json.dump(mock_data, f)
    return json_file


@pytest.fixture
def mock_data():
    """Фикстура для проверки чтения файлов json"""
    return [
        {
            "name": "Category 1",
            "description": "First category",
            "products": [
                {
                    "name": "Product 1",
                    "description": "Description 1",
                    "price": 10.0,
                    "quantity": 5,
                    "color": "Зеленый",
                },
                {
                    "name": "Product 2",
                    "description": "Description 2",
                    "price": 20.0,
                    "quantity": 3,
                    "color": "Красный",
                },
            ],
        },
        {
            "name": "Category 2",
            "description": "Second category",
            "products": [
                {"name": "Product 3", "description": "Description 3", "price": 30.0, "quantity": 2, "color": "Зеленый"}
            ],
        },
    ]


@pytest.fixture
def mixin_product():
    """Фикстура для создания объекта Product с MixinPrint."""
    return Product("Миксер", "Описание миксера", 3000, 10, "Красный")


@pytest.fixture
def order():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "Серый")
    return Order(product=product, quantity=2)


@pytest.fixture
def product():
    """Фикстура для создания тестового продукта."""
    return Product("Тестовый продукт", "Описание тестового продукта", 100, 5, "Красный")


@pytest.fixture
def category_with_products():
    """Фикстура для создания категории с несколькими продуктами."""
    category = Category("Категория с продуктами", "Описание категории")
    category.add_product(Product("Продукт 1", "Описание 1", 100.0, 5, "Красный"))
    category.add_product(Product("Продукт 2", "Описание 2", 200.0, 3, "Синий"))
    return category


@pytest.fixture
def empty_category():
    """Фикстура для создания пустой категории."""
    return Category("Пустая категория", "Описание пустой категории")
