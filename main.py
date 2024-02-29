# Programming Assignment Unit 4
# Andreas Dau, 2024-02-29

from math import sqrt


def hypotenuse(kathete1: float, kathete2: float):
    return sqrt(kathete1 ** 2 + kathete2 ** 2)


print(hypotenuse(3, 4))
