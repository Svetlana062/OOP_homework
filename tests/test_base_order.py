import pytest
from src.product import Product  # Импортируйте нужные классы
from src.order import Order  # Импортируйте класс заказа

@pytest.fixture
def product():
    """Фикстура для создания тестового продукта."""
    return Product('Тестовый продукт', 'Описание тестового продукта', 100, 5, 'Красный')

def test_product_creation(product):
    """Тест создания продукта."""
    assert product.name == 'Тестовый продукт'
    assert product.description == 'Описание тестового продукта'
    assert product.price == 100
    assert product.quantity == 5
    assert product.color == 'Красный'

def test_product_str(product):
    """Тест строкового представления продукта."""
    assert str(product) == 'Тестовый продукт, 100 руб. Остаток: 5 шт. Цвет: Красный'

def test_order_creation(product):
    """Тест создания заказа."""
    order = Order(product, 2)
    assert order.product == product
    assert order.quantity == 2
    assert order.total_cost() == 200  # 100 * 2

def test_order_str(order):
    """Тест строкового представления заказа."""
    order = Order(product, 2)
    assert str(order) == 'Заказ: Тестовый продукт, Количество: 2, Сумма: 200 руб.'
