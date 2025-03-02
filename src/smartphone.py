from src.product import Product


class Smartphone(Product):
    """Класс для смартфонов."""

    efficiency: float  # производительность
    model: str  # модель
    memory: int  # объем встроенной памяти

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color) -> None:
        # Вызов конструктора родительского класса
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory

    def __str__(self):
        """Строковое отображение для класса Smartphone"""
        return (
            super().__str__() + f", Модель: {self.model}, Производительность: {self.efficiency}, Память: {self.memory}"
        )

    def __add__(self, other):
        """Сложение"""
        if type(other) is __class__:
            summ = self.price + other.price
            return summ
        else:
            raise TypeError
