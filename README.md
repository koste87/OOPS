# Online store

## Описание

Интернет-магазин

## Содержание

* модули main.py и config.py в корне проекта
* папка data
* директория tests с тестами к модулям
* директория src с рабочими модулями

**Модули директории src:**
1. *category.py*. В модуле описан класс Category 
```
class Category:
    """Класс для предоставления категорий товаров"""

    name: str
    description: str
    products: list  # приватный атрибут
    category_count = 0
    product_count = 0
```
В классе есть приватный атрибут *products*

2. *base_product.py*. В модуле описан абстрактный класс BaseProduct
```
class BaseProduct(ABC):
    """Абстрактный класс для представления продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
```

3. *product.py*. В модуле описан класс Product
```
class Product:
    """Класс для представления товара"""

    name: str
    description: str
    __price: float
    quantity: int
```
В классе есть приватный атрибут *price*

Для каждого класса прописан метод __str __ для строкового отображения информации в определённом формате:
```
<Название продукта>, n руб. Остаток: m шт.
<Название категории>, количество продуктов: n шт.
```
В классе Product реализована возможность складывать продукты. Итогом сложения является полная стоимость всех товаров на складе.

4. *lawn_grass.py*. Модуль содержит класс LawnGrass, наследуемый от класса Product
```
class LawnGrass(Product):
    """Класс для предствления товаров категории 'Трава газонная'"""
    
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str
```

5. *smartphone.py*. Модуль содержит класс Smartphone, наследуемый от класса Product
```
class Smartphone(Product):
    """Класс для предствления товаров категории 'Смартфоны'"""
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str
```

6. *print_mixin.py*. В модуле описан класс_михин для вывода информации о продукте при его инициализации.
Формат вывода информации о продукте: <ИмяКласса>(название продукта, описание, цена, количество)


7. *utils.py*. В модуле реализована функция для чтения данных из JSON-файла и созания на их основе объектов классов

## Тестировние

В директории tests прописаны тесты для всех модулей директории src.
Также здесь есть модуль conftest.py с фикстурами для тестов. Coverage report: 99%