import unittest

from src.lawn_grass import LawnGrass
from src.product import Product


class TestLawnGrass(unittest.TestCase):

    def setUp(self):
        """Создание экземпляра класса LawnGrass для тестов."""
        self.lawn_grass = LawnGrass(
            name="Газонная трава",
            description="Элитная трава для газона",
            price=500.0,
            quantity=20,
            country="Россия",
            germination_period="7 дней",
            color="Зеленый",
        )

    def test_initialization(self):
        """Тестирование инициализации объекта LawnGrass."""
        self.assertEqual(self.lawn_grass.name, "Газонная трава")
        self.assertEqual(self.lawn_grass.description, "Элитная трава для газона")
        self.assertEqual(self.lawn_grass.price, 500.0)
        self.assertEqual(self.lawn_grass.quantity, 20)
        self.assertEqual(self.lawn_grass.country, "Россия")
        self.assertEqual(self.lawn_grass.germination_period, "7 дней")
        self.assertEqual(self.lawn_grass.color, "Зеленый")
        assert issubclass(LawnGrass, Product)  # Проверка, что LawnGrass является подклассом Product

    def test_str_method(self):
        """Тестирование строкового представления объекта LawnGrass."""
        expected_str = (
            "Газонная трава, 500.0 руб. Остаток: 20 шт. Цвет: ЗеленыйСтрана: Россия, Срок " "прорастания: 7 дней."
        )
        self.assertEqual(str(self.lawn_grass), expected_str)

    def test_country(self):
        """Тестирование атрибута страны."""
        self.assertEqual(self.lawn_grass.country, "Россия")
        self.lawn_grass.country = "Канада"
        self.assertEqual(self.lawn_grass.country, "Канада")

    def test_germination_period(self):
        """Тестирование атрибута срока прорастания."""
        self.assertEqual(self.lawn_grass.germination_period, "7 дней")
        self.lawn_grass.germination_period = "10 дней"
        self.assertEqual(self.lawn_grass.germination_period, "10 дней")

    def test_lawn_grass_is_subclass_of_product(self):
        """Проверка, что LawnGrass является подклассом Product."""
        self.assertTrue(issubclass(LawnGrass, Product))

    def test_lawn_grass_instance(self):
        """Проверка, что экземпляр LawnGrass является экземпляром Product."""
        self.assertIsInstance(self.lawn_grass, Product)

    def test_total_cost(self):
        """Проверка, что метод total_cost возвращает правильное значение."""
        expected_cost = self.lawn_grass.price * self.lawn_grass.quantity  # Ожидаемая стоимость
        self.assertEqual(self.lawn_grass.total_cost(), expected_cost)


if __name__ == "__main__":
    unittest.main()
