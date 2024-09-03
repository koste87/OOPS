from src.classes import Category, Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_init(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert category_1.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_1.products) == 2

    assert Category.category_count == 2
    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 3
    assert category_2.product_count == 3
    assert Category.product_count == 3


def test_category_products_list_property(category_1):
    assert category_1.products_list == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_category_products_setter(category_1, product):
    assert len(category_1.products) == 2
    category_1.add_product = product
    assert len(category_1.products) == 3


def test_product_new_product():
    product = {"name": "Nokia", "description": "Yellow", "price": 90000.0, "quantity": 10}
    new_product = Product.new_product(product)
    assert new_product.name == "Nokia"
    assert new_product.description == "Yellow"
    assert new_product.price == 90000.0
    assert new_product.quantity == 10


def test_price_property(product):
    assert product.price == 180000.0


def test_price_setter(capsys, product):
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 180000.0

    product.price = -99999.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 180000.0

    product.price = 0.1
    assert product.price == 0.1
