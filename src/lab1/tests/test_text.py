import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))

from lib.text import normalize, tokenize, count_freq, top_n


def test_normalize_basic():
    assert normalize("САП МИР") == "сап мир"
    assert normalize("Бладс Бладс") == "бладс бладс"
    print("normalize с базовыми все четко")


def test_normalize_edge_cases():
    assert normalize("") == ""
    assert normalize("  ") == ""
    assert normalize("     Много пробелов       ") == "много пробелов"
    print("normalize с граничными уцы все в порядке")


def test_tokenize_basic():
    result = tokenize("сап ма бой как район")
    assert result == ["сап", "ма", "бой", "как", "район"]

    result2 = tokenize("ты,он и она!")
    assert "ты" in result2 and "она" in result2
    print("tokenize базовые работают")


def test_count_freq_basic():
    tokens = ["черный", "белый", "черный", "белый", "серый"]
    result = count_freq(tokens)
    expected = {"черный": 2, "белый": 2, "серый": 1}
    assert result == expected
    print("count_freq базовые прошли как надо")


def test_top_n_basic():
    freq_dict = {"Мерс": 3, "БМВ": 3, "Audi": 3}
    result = top_n(freq_dict, 2)
    assert result == [("Audi", 3), ("БМВ", 3)]
    print("top_n сортировка при равной частоте прошла на ура")


def test_top_n_tie_breaker():
    freq_dict = {"пингвин": 3, "медведь": 3, "волк": 3}
    result = top_n(freq_dict, 2)
    assert result == [("волк", 3), ("медведь", 3)]
    print("top_n сортировка при равной частоте прошла")
