import math
import re

comparisonOperators = ["<", ">", "<=", ">=", "==", "!="]


# Returns true if the specified string is a number, returns false otherwise
def is_number(string: str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        try:
            int(string)
            return True
        except ValueError:
            return False


# Returns true if the specified string is a float number, returns false otherwise
def is_float_number(string: str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False


# Returns true if the specified expression is an inequality with an absolute value, returns false otherwise
def inequality_with_absolute(expression: str) -> bool:
    args = re.split("\\s+", expression)
    if len(args) != 3:
        return False
    return args[0].startswith("|") and args[0].endswith("|") and not is_number(list(args[0])[1]) and list(args[0])[2] in ["-", "+"] and is_number(args[0][3:][:-1]) and args[1] in comparisonOperators and is_number(args[2])


# Returns true if the number is even, returns false otherwise
def is_even(number: int) -> bool:
    return number % 2 == 0


# Returns true if the number is prime, returns false otherwise
def is_prime(number: int) -> bool:
    for x in range(2, int(number**0.5) + 1):
        if number % x == 0:
            return False
    return True


# Returns true if the number is perfect, returns false otherwise
def is_perfect(number: int) -> bool:
    return sum(get_divisors_without_itself(number)) == number


# Returns a list of the number's divisors without itself
def get_divisors_without_itself(number: int) -> list:
    return [x for x in range(1, int(number / 2) + 1) if number % x == 0]


# Returns a list of the number's divisors
def get_divisors(number: int) -> list:
    lizt = get_divisors_without_itself(number)
    lizt.append(number)
    return lizt