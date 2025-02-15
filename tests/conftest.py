import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_category():
    """Фикстура для теста класса Category, категория "Смартфоны"."""
    category = Category(
        name="Смартфоны",
        description="Смартфоны, как средство коммуникации",
        products=[],  # Передаем пустой список продуктов
    )
    category.add_product(Product("Samsung Galaxy C23", "256GB, Серый цвет, 200MP камера", 24000, 18))
    category.add_product(Product("Iphone 16", "512GB, Gray space", 90000, 13))
    category.add_product(Product("Xiaomi Redmi Note 11S", "1024GB, Синий", 36000, 9))
    return category


@pytest.fixture
def second_category():
    """Фикстура для теста класса Category, категория "Телевизоры"."""
    category = Category(
        name="Телевизоры", description="Современный телевизор", products=[]  # Передаем пустой список продуктов
    )
    category.add_product(Product('55" QLED 4K', "Фоновая подсветка", 124000, 18))
    category.add_product(Product("LG 32LM576BPL", "Широкий формат", 90000, 13))
    category.add_product(Product("Xiaomi TV S Mini LED 55", "Изогнутый экран", 36000, 9))
    category.add_product(Product("Philips 4K Ultra HD", "SMART TV", 34000, 24))
    return category


@pytest.fixture
def product_1():
    """Фикстура для теста класса Products."""
    return Product("Смартфоны", "Описание 1", 24000, 18)


@pytest.fixture
def category_with_products():
    """Фикстура для теста с продуктами."""
    category = Category(name="Тестовая категория", description="Описание категории", products=[])
    product1 = Product.new_product(
        {
            "name": "Телефон",
            "description": "Смартфон",
            "price": 500.0,
            "quantity": 10,
        }
    )
    product2 = Product.new_product(
        {
            "name": "Ноутбук",
            "description": "Игровой ноутбук",
            "price": 1500.0,
            "quantity": 5,
        }
    )
    category.add_product(product1)
    category.add_product(product2)
    return category


@pytest.fixture(autouse=True)
def clear_existing_products():
    """Этот фикстура будет очищать существующие продукты перед каждым тестом."""
    Product.existing_products.clear()


# @pytest.fixture
# def mock_data():
#     """Фикстура для проверки чтения файлов json"""
#     return [
#         {
#             "name": "Category 1",
#             "description": "First category",
#             "products": [
#                 {"name": "Product 1", "description": "Description 1", "price": 10.0, "quantity": 5},
#                 {"name": "Product 2", "description": "Description 2", "price": 20.0, "quantity": 3},
#             ],
#         },
#         {
#             "name": "Category 2",
#             "description": "Second category",
#             "products": [{"name": "Product 3", "description": "Description 3", "price": 30.0, "quantity": 2}],
#         },
#     ]
