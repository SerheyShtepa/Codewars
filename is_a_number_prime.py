"""Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow."""


def is_prime(num: int) -> bool:

    prime_decimal = [2, 3, 5, 7]

    if num in prime_decimal:
        return True
    if (
        num % 2 == 0 or
        num % 3 == 0 or
        num % 5 == 0 or
        num % 7 == 0 or
        num < 0 or
        num == 1
    ):
        return False

    for i in range(7, int(num//2+1), 2):
        if num % i == 0:
            return False

    return True


"""
from math import sqrt
def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):    
        if num%i == 0:
            return False
        i += 1
    return True 
    """
