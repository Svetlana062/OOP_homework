from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


def test_product_iterator():
    # Создаем объект категории с необходимыми аргументами
    category = Category(name="Категория1", description="Описание категории")

    # Добавляем продукты в категорию
    category.add_product(Product("Товар1", "Описание товара 1", 100, 10, "Синий"))
    category.add_product(Product("Товар2", "Описание товара 2", 200, 5, "Серый"))

    # Создаем итератор для категории
    iterator = ProductIterator(category)

    # Преобразуем итератор в список
    products = list(iterator)

    # Проверяем, что количество продуктов верное
    assert len(products) == 2
    assert str(products[0]) == "Товар1, 100 руб. Остаток: 10 шт. Цвет: Синий"
    assert str(products[1]) == "Товар2, 200 руб. Остаток: 5 шт. Цвет: Серый"
