from src.product import Product


class Category:
    """Класс для категории"""

    name: str  # название
    description: str  # описание
    products: list  # список товаров категории

    category_count = 0  # количество категорий
    product_count = 0  # количество продуктов

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


if __name__ == "__main__":
    product = Product("Смартфон", "Серый, Xiaomi", 24000, 18)

    product_1 = Product("Samsung Galaxy C23", "256GB, Серый цвет, 200MP камера", 24000, 18)
    product_2 = Product("Iphone 16", "512GB, Gray space", 90000, 13)
    product_3 = Product("Xiaomi Redmi Note 11S", "1024GB, Синий", 36000, 9)

    category = Category("Смартфоны", "Смартфоны, как средство коммуникации", [product_1, product_2, product_3])

    print(category.name)
    print(category.description)
    print(category.products)

    print(category.category_count)
    print(category.product_count)
