"""Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits..."""


def zeros(n):
    result = 0
    if n < 5:
        return 0
    else:
        x = n // 5
        result += x
        while x >= 5:
            x = x // 5
            result += x
        return result

