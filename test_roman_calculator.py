import pytest

from roman_calculator import roman_to_int


@pytest.mark.parametrize(
    'roman_text,expected', [
        ("I", 1),
        ("IV", 4),
        ("VI", 6),
        ("XI", 11),
        ("XXII", 22),
        ("MMXIX", 2019),
    ])
def test_to_integer(roman_text, expected):
    assert roman_to_int(roman_text) == expected
