
class InvalidRomanInput(Exception):
    pass


roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }


def char_to_int(char: str) -> int:
    try:
        return roman_map[char]
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
        previous_number = char_to_int(roman_text[len(roman_text)-i-1])
        if current_number >= previous_number:
            total += current_number
        else:
            total -= current_number

    return total
