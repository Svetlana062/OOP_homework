from src.order import Order  # Импортируйте класс заказа


def test_product_creation(product):
    """Тест создания продукта."""
    assert product.name == "Тестовый продукт"
    assert product.description == "Описание тестового продукта"
    assert product.price == 100
    assert product.quantity == 5
    assert product.color == "Красный"


def test_product_str(product):
    """Тест строкового представления продукта."""
    assert str(product) == "Тестовый продукт, 100 руб. Остаток: 5 шт. Цвет: Красный"


def test_order_creation(product):
    """Тест создания заказа."""
    order = Order(product, 2)
    assert order.product == product
    assert order.quantity == 2
    assert order.calculate_total() == 200  # 100 * 2


def test_order_str(order):
    """Тест строкового представления заказа."""
    assert str(order) == "Заказ: Samsung Galaxy S23 Ultra, Количество: 2, Итоговая стоимость: 360000.0 " "руб."
