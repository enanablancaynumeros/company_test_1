import pytest

from roman_calculator import roman_to_int, InvalidRomanInput


@pytest.mark.parametrize(
    'roman_text,expected', [
        ("I", 1),
        ("III", 3),
        ("IV", 4),
        ("VI", 6),
        ("XI", 11),
        ("XXII", 22),
        ("CCXXVI", 226),
        ("CM", 900),
        ("MDCCXII", 1712),
        ("MMXIX", 2019),
    ])
def test_to_integer_nice_input(roman_text, expected):
    assert roman_to_int(roman_text) == expected


def test_roman_to_int_exception():
    with pytest.raises(InvalidRomanInput):
        roman_to_int("XO")


def test_roman_to_int_exception_empty():
    with pytest.raises(InvalidRomanInput):
        roman_to_int("")
