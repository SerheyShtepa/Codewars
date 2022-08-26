"""The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return

[F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(n) being the smallest one such as F(n) * F(n+1) > prod."""


# def fib(n):
#     if n <= 0:
#         return 0
#     elif n <= 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

"""код с рекурсией очень медленный"""

def fib(n):
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    else:
        fib1 = 1
        fib2 = 1
        i = 2
        while i < n:
            fib_sum = fib2 + fib1
            fib1 = fib2
            fib2 = fib_sum
            i += 1
        return fib_sum



def productFib(prod):
    result = []
    for i in range(10**10):
        if (fib(i) * fib(i+1)) < prod:
            continue
        else:
            if (fib(i) * fib(i+1)) == prod:
                result.extend([fib(i), fib(i+1), True])
                return result
            elif (fib(i) * fib(i+1)) > prod:
                result.extend([fib(i), fib(i + 1), False])
                return result


"""
def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]
  """