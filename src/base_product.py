from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для представления продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
