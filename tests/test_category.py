def test_category_init_1(first_category, second_category):
    """Тест класса Category"""
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство коммуникации"
    assert len(first_category.products) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 7
    assert second_category.product_count == 7
