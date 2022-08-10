"""In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a
string, and you must return that string in an array where an uppercase letter is a person standing up. """


def wave(people):
    final_wave = []
    for x, y in enumerate(people):
        if y == ' ':
            continue
        else:
            final_wave.append(people[:x] + people[x].upper() + people[x+1:])
    return final_wave


#print(wave('asef wesgr'))
