
class InvalidInput(Exception):
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
        raise InvalidInput(str(e))


def roman_to_int(roman_text: str) -> int:
    total = 0
    i = 0
    while i < len(roman_text):
        first_number = char_to_int(roman_text[i])
        if i == len(roman_text) - 1:
            total += first_number
        else:
            second_number = char_to_int(roman_text[i+1])
            if second_number > first_number:
                total += second_number
                total -= first_number
                i += 1
            else:
                total += first_number
        i += 1

    return total
