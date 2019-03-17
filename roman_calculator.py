class InvalidRomanInput(Exception):
    pass


roman_int_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def char_to_int(char: str) -> int:
    try:
        return roman_int_map[char]
    except KeyError as e:
        raise InvalidRomanInput(str(e))


def roman_to_int(roman_text: str) -> int:
    total = 0

    if len(roman_text):
        total += char_to_int(roman_text[-1])
    else:
        raise InvalidRomanInput(roman_text)

    for i, char in enumerate(reversed(roman_text[:-1])):
        current_number = char_to_int(char)
        previous_number = char_to_int(roman_text[len(roman_text) - i - 1])
        if current_number >= previous_number:
            total += current_number
        else:
            total -= current_number

    return total


def int_to_roman(number: int) -> str:
    combinations = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ""
    for letter, n in zip(combinations, nums):
        result += letter * int(number / n)
        number %= n
    return result


def roman_calculator(roman_text: str) -> str:
    items = roman_text.split()
    