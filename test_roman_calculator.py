import pytest

from api.roman_calculator import (
    roman_to_int,
    InvalidRomanInput,
    int_to_roman,
    roman_calculator,
)


@pytest.mark.parametrize(
    "roman_text,expected",
    [
        ("I", 1),
        ("III", 3),
        ("IV", 4),
        ("VI", 6),
        ("XI", 11),
        ("XXII", 22),
        ("CCXXVI", 226),
        ("CMXC", 990),
        ("MDCCXII", 1712),
        ("MMXIX", 2019),
    ],
)
def test_to_integer_nice_input(roman_text, expected):
    assert roman_to_int(roman_text) == expected


def test_roman_to_int_exception():
    with pytest.raises(InvalidRomanInput):
        roman_to_int("XO")


def test_roman_to_int_exception_empty():
    with pytest.raises(InvalidRomanInput):
        roman_to_int("")


@pytest.mark.parametrize(
    "number,expected",
    [
        (1, "I"),
        (3, "III"),
        (4, "IV"),
        (6, "VI"),
        (11, "XI"),
        (22, "XXII"),
        (226, "CCXXVI"),
        (990, "CMXC"),
        (1712, "MDCCXII"),
        (2019, "MMXIX"),
    ],
)
def test_to_roman_nice_input(number, expected):
    assert int_to_roman(number) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("I + I", "II"),
        ("III - I", "II"),
        ("IV * IV", "XVI"),
        ("VI ^ II", "XXXVI"),
        ("XI - II + X", "XIX"),
        ("(XXI - (II * X))", "I"),
        ("XXII - II * X", "II"),
    ],
)
def test_calculator(text, expected):
    assert roman_calculator(text) == expected
