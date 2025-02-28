import json

import pytest

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
