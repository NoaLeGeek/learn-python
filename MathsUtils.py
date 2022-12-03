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
def is_inequality_with_absolute(expression: str) -> bool:
    return re.match("^\|[a-zA-Z](-|\+)(-?\d+(.\d+)?)\| ((<|>)=?|!=|=) (-?\d+(.\d+)?)$", expression) is not None


# Returns true if the specified expression is an inequality, returns false otherwise
def is_inequality(expression: str) -> bool:
    args = re.split("\s+", expression)
    return re.match(
        "^([a-zA-Z] ((<|>)=?|!=|=) -?\d+(.\d+)?$)$|(^-?\d+(.\d+)? ((<|>)=?|!=|=) [a-zA-Z]$)|(^-?\d+(.\d+)? (?P<operation>(<|>))=? [a-zA-Z] (?P=operation)=? -?\d+(.\d+)?)|((-?\d+(.\d+)? <=? [a-zA-Z])|([a-zA-Z] >=? -?\d+(.\d+)?)) U ((-?\d+(.\d+)? >=? [a-zA-Z])|([a-zA-Z] <=? -?\d+(.\d+)?))|((-?\d+(.\d+)? >=? [a-zA-Z])|([a-zA-Z] <=? -?\d+(.\d+)?)) U ((-?\d+(.\d+)? <=? [a-zA-Z])|([a-zA-Z] >=? -?\d+(.\d+)?))$",
        expression) is not None and (len(args) == 3
                                     or (len(args) == 5 and (float(args[0]) < float(args[4 if len(args) == 5 else 6]) if "<" in args[1] else float(args[0]) > float(args[4 if len(args) == 5 else 6])))
                                     or (len(args) == 7 and (list(filter(is_number, args))[0] < list(filter(is_number, args))[1] if re.match("((-?\d+(.\d+)? >=? [a-zA-Z])|([a-zA-Z] <=? -?\d+(.\d+)?)) U ((-?\d+(.\d+)? <=? [a-zA-Z])|([a-zA-Z] >=? -?\d+(.\d+)?))", expression) is not None else list(filter(is_number, args))[0] > list(filter(is_number, args))[1])))


# Return true if the specified expression is an interval, return false otherwise
def is_interval(expression: str) -> bool:
    args = re.split("\s+", expression)
    return re.match("^[a-zA-Z] (∈|E) (((\[-?\d+(.\d+)?|\](-?\d+(.\d+)?|-(∞|inf)));((-?\d+(.\d+)?|\+?(∞|inf))\[|-?\d+(.\d+)?\])$)|(\]-(∞|inf);-?\d+(.\d+)?)(\[|\]) U (\[|\])(-?\d+(.\d+)?);\+?(∞|inf)\[$)", expression) is not None \
           and ((len(args) == 3
                 and ((args[2].split(";")[0][1:] == "-∞" or "∞" in args[2].split(";")[1][:-1])
                 or float(args[2].split(";")[0][1:]) < float(args[2].split(";")[1][:-1])))
                or (len(args) == 5
                    and float(args[2].split(";")[1][:-1]) < float(args[4].split(";")[0][1:])))


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


# Returns a list of the possible translations of a specified mathematical expression
def translations_expression(expression: str) -> list[str]:
    lizt = []
    if is_inequality(expression):
        # re.search("(?!(\d|U))\w", expression).group(0) is collecting the first alphabetic letter from the expression
        letter = re.search("(?!(\d|U))\w", expression).group(0)
        args = re.split("\s+", expression)
        # Interval translation
        translation = letter + " ∈ " + ("{}{};{}{}" if len(args) != 7 else "{}{};{}{} U {}{};{}{}")
        match len(args):
            case 3:
                if args[1] == "=":
                    translation = translation.format("[", args[2 if is_number(args[2]) else 0], ";", args[2 if is_number(args[2]) else 0], "]")
                elif args[1] == "!=":
                    translation = translation.format("]-∞;", args[2 if is_number(args[2]) else 0], "[ U ]", args[2 if is_number(args[2]) else 0], ";+∞[")
                else:
                    translation = translation.format("]", "-∞", args[0 if is_number(args[0]) else 2], ("]" if "=" in args[1] else "[") if ((is_number(args[0]) and ">" in args[1]) or (not is_number(args[0]) and "<" in args[1])) else ("[" if "=" in args[1] else "]"), args[0 if is_number(args[0]) else 2], "+∞", "[")
            case 5:
                translation = translation.format(("[" if "=" in args[1] else "]"), (args[0] if "<" in args[1] else args[4]), (args[4] if "<" in args[3] else args[0]), ("]" if "=" in args[3] else "["))
            case 7:
                translation = translation.format("]", "-∞", (list(filter(is_number, expression))[0] if re.match("((-?\d+(.\d+)? >=? [a-zA-Z])|([a-zA-Z] <=? -?\d+(.\d+)?)) U ((-?\d+(.\d+)? <=? [a-zA-Z])|([a-zA-Z] >=? -?\d+(.\d+)?))", expression) is not None else list(filter(is_number, expression))[1]), ("]" if "=" in args[1] else "["), ("[" if "=" in args[5] else "]"), (list(filter(is_number, expression))[1] if re.match("((-?\d+(.\d+)? >=? [a-zA-Z])|([a-zA-Z] <=? -?\d+(.\d+)?)) U ((-?\d+(.\d+)? <=? [a-zA-Z])|([a-zA-Z] >=? -?\d+(.\d+)?))", expression) is not None else list(filter(is_number, expression))[0]), "+∞", "[")
        lizt.append(translation)
        # Inequality with absolute value translation
        translation = ""
        if len(args) != 3:
            translation = "|"
        return lizt
    elif is_interval(expression):
        return lizt
    elif is_inequality_with_absolute(expression):
        return lizt
    else:
        raise SyntaxError("The specified expression has no possible translation")



