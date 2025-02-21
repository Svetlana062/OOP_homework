from src.product import Product
from src.product_iterator import ProductIterator


class Category:
    """Класс для категории"""

    name: str  # название
    description: str  # описание
    __products: list  # список товаров категории

    category_count = 0  # количество категорий
    product_count = 0  # количество продуктов

    def __init__(self, name, description, __products=None):
        self.name = name
        self.description = description
        self.__products = []  # Инициализация списка продуктов
        Category.category_count += 1
        Category.product_count += len(self.__products)  # Увеличиваем счетчик продуктов на количество переданных

    def __str__(self):
        """Строковое отображение для класса Category"""
        total_quantity = len(self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __add__(self, other):
        """Складывает стоимость всех продуктов из двух категорий."""
        if isinstance(other, Category):
            total_cost = sum(product.price * product.quantity for product in self.__products)
            total_cost += sum(product.price * product.quantity for product in other.__products)
            return total_cost
        return NotImplemented

    def __iter__(self):
        """Возвращает итератор для продуктов в категории."""
        return ProductIterator(self)

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
        return "\n".join(str(product) for product in self.__products)

    @property
    def get_products(self):
        """Возвращает список продуктов в категории."""
        return self.__products
