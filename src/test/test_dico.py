# A faire après avoir pull le repisotory de Cécile (dico a été modifié)

from src.utils.dico import *


def test_dico():
    assert type(create_dico()[1]) == str


def test_dico_1():
    assert type(create_dico_1()["theatre_antique"]) == int


def test_create_dico_cities_landmarks():
    assert create_dico_cities_landmarks()[1] == "Aix-en-Provence, Pavillon Noir"


if __name__ == "__main__":
    test_dico()
    test_dico_1()
    test_create_dico_cities_landmarks()
