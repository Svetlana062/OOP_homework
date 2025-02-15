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
        self.__products = []  # Приватный атрибут для хранения списка товаров
        Category.category_count += 1

    def add_product(self, product: Product):
        """Добавляет продукт в категорию, если это объект класса Product."""
        if isinstance(product, Product):  # Проверяем, что передан объект класса Product
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Передан неверный тип. Ожидался объект класса Product.")

    @property
    def products(self):
        """Геттер для просмотра списка товаров в виде строк."""
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]
        )
