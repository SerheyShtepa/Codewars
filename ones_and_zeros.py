def binary_array_to_number(arr):
    n = ''.join(map(str, arr))
    return int(n, 2)


print(binary_array_to_number([0, 0, 0, 1]))