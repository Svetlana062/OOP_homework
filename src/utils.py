import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """Чтение json-файлов"""
    full_path = os.path.abspath(path)
    try:
        with open(full_path, "r", encoding="UTF-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def create_objects_from_json(data: dict) -> list:
    """Создание объектов из json-файлов"""
    categories = []
    for category_data in data:
        # Создаем объект Category без передачи products
        category = Category(name=category_data["name"], description=category_data["description"])
        for product_data in category_data["products"]:
            product = Product(**product_data)  # Создаем объект Product
            category.add_product(product)  # Добавляем продукт в категорию
        categories.append(category)

    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    categories_data = create_objects_from_json(raw_data)
    print(categories_data[0].name)
    print(categories_data[1].name)
