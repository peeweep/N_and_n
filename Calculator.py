from math import pi, tan
from decimal import Decimal


def decimal_power(x, y=2):
    return Decimal(x) ** Decimal(y)


if __name__ == "__main__":
    __LAMBDA__ = Decimal(input("Type __LAMBDA__'s value:\t")
                         ) * decimal_power(x=10, y=-3)
    __PI__ = Decimal(pi)
    __D__ = Decimal(Decimal(3) * decimal_power(Decimal(10), Decimal(-6)))
    __SQUARE_LAMBDA__ = __LAMBDA__ ** Decimal(2)
    n = (1 +
         (Decimal(2.4885) * __SQUARE_LAMBDA__) /
         (__SQUARE_LAMBDA__ - decimal_power(102.30))
         +
         (Decimal(2.215) * __SQUARE_LAMBDA__) /
         (__SQUARE_LAMBDA__ - decimal_power(372.60))
         +
         (Decimal(0.2550) * __SQUARE_LAMBDA__) /
         (__SQUARE_LAMBDA__ - decimal_power(1850))
         ) ** Decimal(1/2)
    print("The value of n is {}".format(n))
    print("\talmost at {}".format(round(n, 3)))
    N = decimal_power(
        (Decimal(3) * decimal_power(3, Decimal(1/2)) * n * __D__)
        /
        (Decimal(2) * __LAMBDA__)
        -
        Decimal(6) / __PI__ *
        decimal_power(tan(
            n * decimal_power(Decimal(3) * decimal_power(n) - Decimal(4), y=-1)
        ), y=-1),  y=-1)
    print("The value of N is {}".format(N))
    print("\talmost at {}".format(round(N, 3)))
