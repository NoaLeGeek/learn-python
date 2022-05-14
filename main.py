from random import randint

import Polygon
import Utils
import Games
import MathsUtils
import math


def main():
    x = 0
    y = randint(0, 100)
    while y != 1:
        y = math.floor(y / 2)
        print(y)
        x += 1
    print(x)
    print(x * 1.5)
    Games.guess_number()


if __name__ == '__main__':
    main()
