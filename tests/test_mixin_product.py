import sys
from io import StringIO

from src.mixin_product import MixinProduct


# Предполагается, что у вас есть класс, который наследует MixinPrint
class Product(MixinProduct):
    def __init__(self, name, description, price, quantity, color):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.color = color
        super().__init__()  # Вызываем конструктор MixinPrint


def test_mixin_print_output(mixin_product, capsys):
    """Тест для проверки вывода информации о создании объекта."""
    # Перенаправляем вывод в StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    # Создаем новый объект, который вызовет __init__ и вывод
    Product("Блендер", "Описание блендера", 5000, 5, "Синий")

    # Возвращаем вывод обратно в стандартный вывод
    sys.stdout = sys.__stdout__

    # Получаем результат вывода
    output = captured_output.getvalue()

    # Проверяем, что вывод содержит информацию о создании объекта
    assert "Product(Блендер, Описание блендера, 5000, 5)" in output
    assert "Миксер" not in output  # Убедимся, что не выводится предыдущий объект


def test_product_repr(mixin_product):
    """Тест для проверки корректности представления объекта."""
    assert repr(mixin_product) == "Product(Миксер, Описание миксера, 3000, 10)"
