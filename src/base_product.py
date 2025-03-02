from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс, родительский для класса Product."""

    @abstractmethod
    def __str__(self):
        """Строковое представление продукта."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Сложение продуктов."""
        pass

    @abstractmethod
    def total_cost(self):
        """Метод для вычисления общей стоимости заказа."""
        pass
