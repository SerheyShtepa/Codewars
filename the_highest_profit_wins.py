"""Story
Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

Task
Write a function that returns both the minimum and maximum number of the given list/array.

"""


def min_max(lst):
    new_lst = []
    min_lst = min(lst)
    max_lst = max(lst)
    new_lst.append(min_lst)
    new_lst.append(max_lst)
    return new_lst


print(min_max([1, 2, 3]))