from src.category import Category


def test_category_init_1(first_category, second_category):
    """Тест класса Category"""
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство коммуникации"
    assert len(first_category.products) == 3

    assert Category.category_count == 2
    assert Category.product_count == 7
