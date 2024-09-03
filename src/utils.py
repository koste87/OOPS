import json
import os

from config import DATA_DIR
from src.classes import Category, Product


def read_json(filename: str) -> object:
    """Считывает данные из JSON-файла и на их основе создает объекты классов"""
    file_path = os.path.join(DATA_DIR, filename)

    with open(file_path, encoding="utf-8") as file:
        products_data = json.load(file)

    categories = []

    for category in products_data:
        products = []

        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products

        categories.append(Category(**category))

    return categories
