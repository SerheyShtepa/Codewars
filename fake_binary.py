"""Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
Return the resulting string.

Note: input will never be an empty string"""


def fake_bin(x):
    new_array = []
    x = list(x)
    for i in x:
        if int(i) < 5:
            new_array.append('0')
        else:
            new_array.append('1')
    return ''.join(new_array)
