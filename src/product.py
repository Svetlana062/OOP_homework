class Product:
    """Класс для продуктов"""

    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    product = Product("Смартфоны", "Смартфоны, как средство коммуникации", 24000, 18)
    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)
