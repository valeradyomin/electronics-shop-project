import csv


class InstantiateCSVError(Exception):
    """
    Класс определяет пользовательское исключение.
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден.'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        """
        Геттер приватного атрибута класса
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Сеттер приватного атрибута класса
        """
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[0:10]

    @classmethod
    def instantiate_from_csv(cls, path_to_csv="../src/items.csv"):
        """
        Класс метод для создания объектов из данных файла. Использует перехват исключений.
        """
        cls.all.clear()
        try:
            with open(path_to_csv, newline="", encoding="windows-1251") as csvfile:
                reader = csv.DictReader(csvfile)
                items_objs_lst = []
                for row in reader:
                    if len(row) == 3:
                        items_objs_lst.append(cls(name=row["name"], price=row["price"], quantity=row["quantity"]))
                    else:
                        raise InstantiateCSVError
            return items_objs_lst
        except FileNotFoundError:
            print("Отсутствует файл item.csv")
            return None
        except InstantiateCSVError as error:
            print(error)
            return None

    @staticmethod
    def string_to_number(args: str):
        """
        Статический метод, возвращающий число из числа-строки
        """
        if "." in args:
            args = args.split(".")[0]
            return int(args)
        else:
            return int(args)

    def __repr__(self):
        """
        Репрезентация полей класса
        """
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Отображение информации об объекте класса для пользователей
        """
        return f"{self.name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total = self.price * self.quantity
        return total

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    def __add__(self, other):
        """
        Переопределение магического метода для сложения количества товаров с проверкой
        """
        if not isinstance(other, Item):
            raise ValueError("Складывать можно только объекты Item и дочерние от них")
        return self.quantity + other.quantity
