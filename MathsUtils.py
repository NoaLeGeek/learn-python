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
    return re.match("^\|[a-zA-Z](-|\+)(-?\d+(.\d+)?)\| ((<|>)=?|!=|=) (-?\d+(.\d+)?)$", expression) is not None


# Returns true if the specified expression is an inequality, returns false otherwise
def is_inequality(expression: str) -> bool:
    args = re.split("\s+", expression)
    return re.match(
        "(^[a-zA-Z] ((<|>)=?|!=|=) (-?\d+(.\d+)?$)$)|(^(-?\d+(.\d+)?) ((<|>)=?|!=|=) [a-zA-Z]$)|(^(-?\d+(.\d+)?) (?P<operation>(<|>))=? (?P<letter>[a-zA-Z]) ((U (?P=letter) (?=(?!(!=|=)))(?P=operation) (-?\d+(.\d+)?))|((?P=operation)=? (-?\d+(.\d+)?)))$)",
        expression) is not None and args[1] == args[3] and (((float(args[0]) if is_float_number(args[0]) else int(
        args[0])) < (float(args[4]) if is_float_number(args[4]) else int(args[4]))) if "<" in args[1] else (
                (float(args[4]) if is_float_number(args[4]) else int(args[4])) > (
            float(args[0]) if is_float_number(args[0]) else int(args[0]))))


# Return true if the specified expression is an interval, return false otherwise
def is_interval(expression: str) -> bool:
    args = re.split("\s+", expression)
    return re.match("^[a-zA-Z] (∈|E) (((\[|\])(-∞|(-?\d+(.\d+)?));(\+?∞|(-?\d+(.\d+)?))(\[|\])$)|(\]-∞;(-?\d+(.\d+)?)(\[|\]) U (\[|\])(-?\d+(.\d+)?);\+?∞\[$))", expression) is not None and ((len(args) == 5 and (float(args[2].split(";")[1][:-1]) if is_float_number(args[2].split(";")[1][:-1]) else int(args[2].split(";")[1][:-1])) < (float(args[4].split(";")[0][1:]) if is_float_number(args[4].split(";")[0][1:]) else int(args[4].split(";")[0][1:])) and args[2].split(";")[-1] != args[4].split(";")[0]) or (len(args) == 3 and ((args[2].split(";")[0][1:] == "-∞" or args[2].split(";")[1][:-1] in ["∞", "+∞"]) or (float(args[2].split(";")[0][1:]) if is_float_number(args[2].split(";")[0][1:]) else int(args[2].split(";")[0][1:])) < (float(args[2].split(";")[1][:-1]) if is_float_number(args[2].split(";")[1][:-1]) else int(args[2].split(";")[1][:-1])))))


# Returns true if the number is even, returns false otherwise
def is_even(number: int) -> bool:
    return number % 2 == 0


# Returns true if the number is prime, returns false otherwise
def is_prime(number: int) -> bool:
    for x in range(2, int(number ** 0.5) + 1):
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
