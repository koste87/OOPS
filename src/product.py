from src.base_product import BaseProduct
from src.print_mixin import PrintMixin

class Product(BaseProduct, PrintMixin):
    """Класс для представления товара"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        """Метод для строкового отображения информации о товаре"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_dict: dict) -> "Product":
        """Создаёт новый экземпляр класса Product из словаря"""
        return cls(**product_dict)

    @property
    def price(self) -> float:
        """Возвращает цену товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Возвращает сообщение об ошибке, если цена меньше или равна нулю"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __add__(self, other) -> float:
        """Суммирует цену всех экземпляров, имеющихся на складе, для двух товаров"""
        if type(other) is self.__class__:
            price_1 = self.__price * self.quantity
            price_2 = other.__price * other.quantity

            return price_1 + price_2

        raise TypeError
