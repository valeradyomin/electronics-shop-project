"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

import pytest

from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test__repr__(item1):
    assert item1.__repr__() == "Item('name=Смартфон', 'price=10000', 'quantity=20')"


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    Item.pay_rate = 1.0
    item1.apply_discount()
    assert item1.price == 10000


def test_private_name(item1):
    assert item1.name == item1._Item__name


def test_setter_name(item1):
    item1.name = "Смартфон"
    assert item1.name == "Смартфон"


def test_setter_long_name(item1):
    item1.name = "СуперСмартфон"
    assert item1.name == "СуперСмарт"


@pytest.fixture
def items_csv(tmp_path):
    csv_file = tmp_path / "items.csv"
    with open(csv_file, "w", newline="", encoding="windows-1251") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "price", "quantity"])
        writer.writeheader()
        writer.writerow({"name": "Item 1", "price": "10", "quantity": "5"})
        writer.writerow({"name": "Item 2", "price": "15.0", "quantity": "3"})
    return csv_file


def test_instantiate_from_csv(items_csv):
    items = Item.instantiate_from_csv(items_csv)
    assert len(items) == 2
    assert items[0].name == "Item 1"
    assert items[0].price == str(10)
    assert items[0].quantity == str(5)
    assert items[1].name == "Item 2"
    assert items[1].price == str(15.0)
    assert items[1].quantity == str(3)


def test_string_to_number():
    assert Item.string_to_number("10.0") == 10
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("7.8") == 7
    assert Item.string_to_number("3.14") == 3
