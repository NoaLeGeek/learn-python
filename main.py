import re
from random import randint

import Polygon
import Utils
import Games
import MathsUtils
import math


def main():
    x = input("enter a inequality, interval or absolute value inequality:\n")
    print(MathsUtils.translations_expression(x))


if __name__ == '__main__':
    main()
