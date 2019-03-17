import ast
import operator


class InvalidRomanInput(Exception):
    pass


class InvalidCalculatorInput(Exception):
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
    combinations = [
        "M",
        "CM",
        "D",
        "CD",
        "C",
        "XC",
        "L",
        "XL",
        "X",
        "IX",
        "V",
        "IV",
        "I",
    ]
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ""
    for letter, n in zip(combinations, nums):
        result += letter * int(number / n)
        number %= n
    return result


def roman_calculator(roman_text: str) -> str:
    """
    To simplify errors feedback, we will simply catch any exception
    """
    try:
        number = Calc.evaluate(roman_text)
        return int_to_roman(number)
    except Exception:
        raise InvalidCalculatorInput('Invalid expression')


_OP_MAP = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.floordiv,
    ast.BitXor: operator.pow,
}


class Calc(ast.NodeVisitor):
    """
    Extended from https://stackoverflow.com/questions/33029168/how-to-calculate-an-equation-in-a-string-python
    """

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return _OP_MAP[type(node.op)](left, right)

    def visit_Name(self, node):
        return roman_to_int(node.id)

    def visit_Expr(self, node):
        return self.visit(node.value)

    @classmethod
    def evaluate(cls, expression):
        tree = ast.parse(expression)
        calc = cls()
        return calc.visit(tree.body[0])
