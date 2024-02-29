# Programming Assignment Unit 4
# Andreas Dau, 2024-02-29

from math import sqrt


def hypotenuse(kathete1: float, kathete2: float):

    if kathete1 >= 0 and kathete2 >= 0:
        return sqrt(kathete1 ** 2 + kathete2 ** 2)
    else:
        raise ValueError("The legs of a triangle can't be negative.")


print(hypotenuse(-3, -4))
