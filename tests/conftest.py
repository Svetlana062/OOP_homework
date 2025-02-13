import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_category():
    """Фикстура для теста класса Category"""
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство коммуникации",
        products=[
            Product("Samsung Galaxy C23", "256GB, Серый цвет, 200MP камера", 24000, 18),
            Product("Iphone 16", "512GB, Gray space", 90000, 13),
            Product("Xiaomi Redmi Note 11S", "1024GB, Синий", 36000, 9),
        ],
    )


@pytest.fixture
def second_category():
    """Фикстура для теста класса Category"""
    return Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=[
            Product('55" QLED 4K', "Фоновая подсветка", 124000, 18),
            Product("LG 32LM576BPL", "Широкий формат", 90000, 13),
            Product("Xiaomi TV S Mini LED 55", "Изогнутый экран", 36000, 9),
            Product("Philips 4K Ultra HD", "SMART TV", 34000, 24),
        ],
    )


@pytest.fixture
def products():
    """Фикстура для теста класса Products"""
    return Product("Смартфоны", "Смартфоны, как средство коммуникации", 24000, 18)


@pytest.fixture
def mock_data():
    """Фикстура для проверки чтения файлов json"""
    return [
        {
            "name": "Category 1",
            "description": "First category",
            "products": [
                {"name": "Product 1", "description": "Description 1", "price": 10.0, "quantity": 5},
                {"name": "Product 2", "description": "Description 2", "price": 20.0, "quantity": 3}
            ]
        },
        {
            "name": "Category 2",
            "description": "Second category",
            "products": [
                {"name": "Product 3", "description": "Description 3", "price": 30.0, "quantity": 2}
            ]
        }
    ]
