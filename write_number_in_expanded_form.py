"""You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
"""


def expanded_form(num):
    nums = []
    f = str(num)
    for x, y in enumerate(f):
        if y == '0':
            continue
        else:
            nums.append(str(f[x])+str('0' * len(f[x+1:])))
    return ' + '.join(nums)


print(expanded_form(102))
