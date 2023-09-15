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
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[0:10]

    @classmethod
    def instantiate_from_csv(cls, args):
        cls.all.clear()
        with open(args, newline="", encoding="windows-1251") as csvfile:
            reader = csv.DictReader(csvfile)
            items_objs_lst = []
            for row in reader:
                items_objs_lst.append(cls(name=row["name"], price=row["price"], quantity=row["quantity"]))
        return items_objs_lst

    @staticmethod
    def string_to_number(args: str):
        if "." in args:
            args = args.split(".")[0]
            return int(args)
        else:
            return int(args)

    def __repr__(self):
        return f"Item('name={self.name}', 'price={self.price}', 'quantity={self.quantity}')"

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
