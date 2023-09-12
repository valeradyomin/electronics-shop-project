"""Здесь надо написать тесты с использованием pytest для модуля item."""
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
