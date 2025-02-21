class ProductIterator:
    """Вспомогательный класс, с помощью которого можно перебирать товары одной категории"""

    def __init__(self, category):
        self._category = category
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        products = self._category.get_products  # Используем метод для получения продуктов
        if self._index < len(products):
            product = products[self._index]
            self._index += 1
            return product
        else:
            raise StopIteration
