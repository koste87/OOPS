import pytest


def test_smartphone_init(grass1):
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_lawn_grass_add(grass1, grass2):
    assert grass1 + grass2 == 16750


def test_lawn_grass_add_error(grass1, smartphone1):
    with pytest.raises(TypeError):
        res1 = grass1 + smartphone1
        res2 = grass1 + 1
