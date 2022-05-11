import math


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
