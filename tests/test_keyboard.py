import pytest

from src.keyboard import Keyboard


@pytest.fixture
def keyboard1():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_init(keyboard1):
    keyboard2 = Keyboard('test', 1000, 1)
    assert keyboard1.name == "Dark Project KD87A"
    assert keyboard1.price == 9600
    assert keyboard1.quantity == 5
    assert keyboard1.language == "EN"
    assert keyboard1.language == keyboard2.language


def test_change_lang(keyboard1):
    keyboard1.change_lang()
    assert keyboard1.language == "RU"
    keyboard1.change_lang()
    assert keyboard1.language == "EN"
