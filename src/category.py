from src.product import Product


class Category:
    """Класс для предоставления категорий товаров"""

    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Метод для строкового отображения информации о категории"""
        quantity = sum([product.quantity for product in self.__products])

        return f"{self.name}, количество продуктов: {quantity}"

    @property
    def products(self) -> str:
        """Возвращает список товара в виде строки"""
        product_str = ""
        for product in self.__products:
            product_str += str(product) + "\n"

        return product_str

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в список продуктов категории"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError
