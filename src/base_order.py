from abc import ABC, abstractmethod


class BaseOrder(ABC):
    """Базовый абстрактный класс, родительский для класса Order и Category."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self):
        """Строковое представление объекта."""
        pass
