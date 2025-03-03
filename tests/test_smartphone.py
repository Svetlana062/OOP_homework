import unittest

from src.product import Product
from src.smartphone import Smartphone


class TestSmartphone(unittest.TestCase):

    def setUp(self):
        """Создание экземпляра класса Smartphone для тестов."""
        self.smartphone = Smartphone(
            name="Samsung Galaxy S23 Ultra",
            description="256GB, Серый цвет, 200MP камера",
            price=180000.0,
            quantity=5,
            efficiency=95.5,
            model="S23 Ultra",
            memory=256,
            color="Серый",
        )

    def test_initialization(self):
        """Тестирование инициализации объекта Smartphone."""
        self.assertEqual(self.smartphone.name, "Samsung Galaxy S23 Ultra")
        self.assertEqual(self.smartphone.description, "256GB, Серый цвет, 200MP камера")
        self.assertEqual(self.smartphone.price, 180000.0)
        self.assertEqual(self.smartphone.quantity, 5)
        self.assertEqual(self.smartphone.efficiency, 95.5)
        self.assertEqual(self.smartphone.model, "S23 Ultra")
        self.assertEqual(self.smartphone.memory, 256)
        self.assertEqual(self.smartphone.color, "Серый")

    def test_str_method(self):
        """Тестирование строкового представления объекта Smartphone."""
        expected_str = (
            "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт. Цвет: Серый, Модель: "
            "S23 Ultra, Производительность: 95.5, Память: 256"
        )
        self.assertEqual(str(self.smartphone), expected_str)

    def test_efficiency(self):
        """Тестирование атрибута эффективности."""
        self.assertEqual(self.smartphone.efficiency, 95.5)
        self.smartphone.efficiency = 90.0
        self.assertEqual(self.smartphone.efficiency, 90.0)

    def test_quantity(self):
        """Тестирование атрибута количества."""
        self.assertEqual(self.smartphone.quantity, 5)
        self.smartphone.quantity = 10
        self.assertEqual(self.smartphone.quantity, 10)

    def test_smartphone_is_subclass_of_product(self):
        """Проверка, что Smartphone является подклассом Product."""
        self.assertTrue(issubclass(Smartphone, Product))

    def test_smartphone_instance(self):
        """Проверка, что экземпляр Smartphone является экземпляром Product."""
        self.assertIsInstance(self.smartphone, Product)

    def test_total_cost(self):
        """Проверка, что метод total_cost возвращает правильное значение."""
        expected_cost = 180000.0 * 5  # Ожидаемая стоимость
        self.assertEqual(self.smartphone.total_cost(), expected_cost)


if __name__ == "__main__":
    unittest.main()
