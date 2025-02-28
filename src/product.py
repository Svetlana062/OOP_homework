class Product:
    """Класс для продуктов"""

    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии
    color: str  # цвет

    existing_products = []  # имеющиеся продукты

    def __init__(self, name, description, price, quantity, color):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для цены
        self.quantity = quantity
        self.color = color

    def __str__(self):
        """Строковое отображение для класса Product"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. Цвет: {self.color}"

    def __add__(self, other):
        """Сложение"""
        if not isinstance(other, Product):
            raise TypeError(f"Нельзя сложить {type(self).__name__} и {type(other).__name__}.")

        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_info: dict):
        """Создает новый продукт или обновляет существующий в зависимости от наличия"""
        name = product_info.get("name")
        description = product_info.get("description")
        price = product_info.get("price")
        quantity = product_info.get("quantity")
        color = product_info.get("color")

        for product in cls.existing_products:  # Проверка на наличие существующего товара
            if product.name == name:
                product.quantity += quantity  # Обновляем количество и цену, если товар уже существует
                product.price = max(product.price, price)  # Оставляем более высокую цену
                product.color = color  # Обновляем цвет
                print(
                    f"Товар '{name}' обновлен. Новое количество: {product.quantity},"
                    f"Новая цена: {product.price}, Цвет: {product.color}."
                )
                return product  # Возвращаем обновленный продукт

        # Если товара нет, создаем новый
        new_product = cls(name, description, price, quantity, color)
        cls.existing_products.append(new_product)  # Добавляем новый продукт в список существующих
        print(f"Создан новый товар: {name}, Цена: {price}, Количество: {quantity}, Цвет: {color}.")
        return new_product

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        elif new_price < self.__price:
            confirmation = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {new_price}? (y/n): ")
            if confirmation.lower() != "y":
                print("Изменение цены отменено.")
                return

        self.__price = new_price
        print(f"Цена обновлена на {self.name}: новая цена {self.__price}")
