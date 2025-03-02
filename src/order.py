from src.base_order import BaseOrder
from src.product import Product


class Order(BaseOrder):
    """Класс для заказов, который содержит информацию о товаре и его количестве."""

    def __init__(self, product: Product, quantity: int):
        super().__init__(name=product.name, description=product.description)
        self.product = product
        self.quantity = quantity
        self.total_price = self.calculate_total()

    def calculate_total(self):
        """Метод для расчета общей стоимости заказа."""
        return self.product.price * self.quantity

    def __str__(self):
        return f"Заказ: {self.name}, Количество: {self.quantity}, Итоговая стоимость: {self.total_price} руб."
