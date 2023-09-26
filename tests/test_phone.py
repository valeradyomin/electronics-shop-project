import pytest

from src.phone import Phone


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test__repr__(phone1):
    assert phone1.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim_setter(phone1):
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3

    with pytest.raises(ValueError):
        phone1.number_of_sim = 0

    with pytest.raises(ValueError):
        phone1.number_of_sim = -1

    with pytest.raises(ValueError):
        phone1.number_of_sim = "abc"
