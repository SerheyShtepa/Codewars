"""This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"""


def accum(s):
    result = []
    for x, y in enumerate(s):
        result.append(y.upper() + y.lower() * x)
    return '-'.join(result)

print(accum('FiFa'))