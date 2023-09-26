from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        Репрезентация полей класса
        """
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Геттер приватного атрибута
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        """
        Сеттер приватного атрибута с проверкой допуска принимаемых величин
        """
        if isinstance(number, int) and number > 0:
            self.__number_of_sim = number
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
