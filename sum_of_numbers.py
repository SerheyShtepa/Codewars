"""Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including
them and return it. If the two numbers are equal return a or b."""


def get_sum(a, b):
    if a == b:
        return a
    else:
        if a < b:
            x = a
            y = b
        else:
            y = a
            x = b
        arr = range(x, y+1)
        return sum(arr)


"""def get_sum(a, b):
    return sum(range(min(a, b), max(a, b)+1))"""

