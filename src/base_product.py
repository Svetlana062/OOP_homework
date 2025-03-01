from abc import  ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс, родительский для класса Product."""

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass
