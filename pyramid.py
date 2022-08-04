n_floor = 8
result = []
width = (n_floor * 2) - 1
for x in range(1, 2 * n_floor, 2):
    stars = x * '*'
    line = stars.center(width)
    result.append(line)
print(str('{}\n'*len(result)).format(*result))
cou