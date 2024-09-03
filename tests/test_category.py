import pytest

from src.category import Category


def test_category_init(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert category_1.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_1.products.split("\n")) - 1 == 2

    assert Category.category_count == 4
    assert category_1.category_count == 4
    assert category_2.category_count == 4

    assert category_1.product_count == 7
    assert category_2.product_count == 7
    assert Category.product_count == 7


def test_category_products_list_property(category_1):
    assert category_1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_category_add_product(category_1, product):
    before = len(category_1.products.split("\n"))
    category_1.add_product(product)
    assert len(category_1.products.split("\n")) == before + 1


def test_str_category(category_1, category_2):
    assert str(category_1) == "Смартфоны, количество продуктов: 13"
    assert str(category_2) == "Телевизоры, количество продуктов: 7"


def test_category_add_product_error(category_1):
    with pytest.raises(TypeError):
        category_1.add_product("Product")


def test_category_products_add_product_smartphone(category_1, smartphone1):
    category_1.add_product(smartphone1)
    assert category_1.products.split("\n")[-2] == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_category_middle_price(category_1, category_2):
    assert category_1.middle_price() == 195000
    assert category_2.middle_price() == 123000


def test_category_middle_price_empty():
    cat = Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        products=[],
    )
    assert cat.middle_price() == 0
