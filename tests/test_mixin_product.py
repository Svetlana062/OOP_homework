import pytest
from io import StringIO
from contextlib import redirect_stdout
from src.mixin_product import MixinProduct


# Временный класс для тестирования MixinProduct
class TestProduct(MixinProduct):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Тест для проверки вывода информации о создании объекта
def test_mixin_product_initialization():
    # Перенаправляем стандартный вывод в StringIO
    f = StringIO()
    with redirect_stdout(f):
        product = TestProduct(name="Тестовый продукт", description="Описание", price=100.0, quantity=10,
                              color="Красный")

    # Получаем вывод
    output = f.getvalue().strip()

    # Проверяем, что вывод содержит ожидаемую информацию
    assert "Создан объект класса TestProduct с параметрами:" in output
    assert "name='Тестовый продукт'" in output
    assert "description='Описание'" in output
    assert "price=100.0" in output
    assert "quantity=10" in output
    assert "color='Красный'" in output


# Запуск тестов
if __name__ == "__main__":
    pytest.main()