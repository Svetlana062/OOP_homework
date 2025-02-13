def test_product_init(products):
    """Тест класса Products"""
    assert products.name == "Смартфоны"
    assert products.description == "Смартфоны, как средство коммуникации"
    assert products.price == 24000
    assert products.quantity == 18
