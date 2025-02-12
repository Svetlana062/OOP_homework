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
