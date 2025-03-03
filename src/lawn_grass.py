from src.product import Product


class LawnGrass(Product):
    """Класс для травы газонной."""

    country: str  # страна - производитель
    germination_period: str  # срок прорастания

    def __init__(self, name, description, price, quantity, country, germination_period, color) -> None:
        # Вызов конструктора родительского класса
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period

    def __str__(self):
        """Строковое отображение для класса LawnGrass"""
        return super().__str__() + f"Страна: {self.country}, Срок прорастания: {self.germination_period}."

    def __add__(self, other):
        """Сложение"""
        if isinstance(other, LawnGrass):
            summ = self._Product__price + other._Product__price  # Используем защищенный атрибут
            return summ
        else:
            raise TypeError("Можно складывать только с объектами LawnGrass.")

    def total_cost(self):
        """Метод для вычисления общей стоимости газонной травы."""
        return self._Product__price * self.quantity
