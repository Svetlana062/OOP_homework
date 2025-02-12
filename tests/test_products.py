def test_product_init(products):
    assert products.name == "Смартфоны"
    assert products.description == "Смартфоны, как средство коммуникации"
    assert products.price == 24000
    assert products.quantity == 18
