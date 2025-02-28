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
        if __products is not None:
            Category.product_count += len(self.__products)  # Увеличиваем счетчик продуктов на количество переданных

    def __str__(self):
        """Строковое отображение для класса Category"""
        total_quantity = len(self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    # def __add__(self, other):
    #     """Складывает стоимость всех продуктов из двух категорий."""
    #     if isinstance(other, Category):
    #         total_cost = sum(product.price * product.quantity for product in self.__products)
    #         total_cost += sum(product.price * product.quantity for product in other.__products)
    #         return total_cost
    #     return NotImplemented

    def __add__(self, other):
        if not isinstance(other, Category):
            raise TypeError("Нельзя сложить категории с разными типами.")

        # Проверка на соответствие типов продуктов
        if self.products and other.products:
            isinstance_first_product = type(self.products[0])
            for product in self.products:
                if type(product) is not isinstance_first_product:
                    raise TypeError(
                        f"Нельзя складывать продукты разных типов: {type(product).__name__} и "
                        f"{type(other.products[0]).__name__}."
                    )

            isinstance_second_product = type(other.products[0])
            for product in other.products:
                if type(product) is not isinstance_second_product:
                    raise TypeError(
                        f"Нельзя складывать продукты разных типов: {type(product).__name__} и "
                        f"{type(self.products[0]).__name__}."
                    )

        total_cost = sum(product.price * product.quantity for product in self.products)
        total_cost += sum(product.price * product.quantity for product in other.products)
        return total_cost

    def __iter__(self):
        """Возвращает итератор для продуктов в категории."""
        return ProductIterator(self)

    def add_product(self, product: Product):
        """Добавляет продукт в категорию, если это объект класса Product или его подклассов."""
        if isinstance(product, Product):  # Проверяем, что передан объект класса Product или его подклассов
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Передан неверный тип. Ожидался объект класса Product.")

    @property
    def products(self):
        """Геттер для получения списка товаров в категории."""
        return self.__products  # Возвращаем список продуктов

    @property
    def get_products(self):
        """Возвращает список продуктов в категории."""
        return self.__products

    def products_info(self):
        """Возвращает строку с информацией о продуктах в категории."""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products
        )
