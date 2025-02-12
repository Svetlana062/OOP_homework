import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_category():
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
    return Product("Смартфоны", "Смартфоны, как средство коммуникации", 24000, 18)
