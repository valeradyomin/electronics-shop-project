import csv


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
        геттер приватного атрибута класса
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        сеттер приватного атрибута класса
        """
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[0:10]

    @classmethod
    def instantiate_from_csv(cls, args):
        """
        класс-метод, инициализирующий экземпляры класса данными из файла *.csv
        """
        cls.all.clear()
        with open(args, newline="", encoding="windows-1251") as csvfile:
            reader = csv.DictReader(csvfile)
            items_objs_lst = []
            for row in reader:
                items_objs_lst.append(cls(name=row["name"], price=row["price"], quantity=row["quantity"]))
        return items_objs_lst

    @staticmethod
    def string_to_number(args: str):
        """
        статический метод, возвращающий число из числа-строки
        """
        if "." in args:
            args = args.split(".")[0]
            return int(args)
        else:
            return int(args)

    def __repr__(self):
        """
        репрезентация полей класса
        """
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        отображения информации об объекте класса для пользователей
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
