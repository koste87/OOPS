from src.product import Product


class Smartphone(Product):
    """Класс для предствления товаров категории 'Смартфоны'"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """Метод для инициализации экземпляра класса"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
