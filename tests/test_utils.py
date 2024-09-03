from unittest.mock import patch

from src.product import Product
from src.utils import read_json


@patch("json.load")
def test_read_json(mock_json, products_json):
    mock_json.return_value = products_json
    data = read_json("products.json")
    assert data[0].name == "Смартфоны"
    assert data[1].products.strip() == str(Product('55"', "Фоновая подсветка", 123000.0, 7)).strip()
