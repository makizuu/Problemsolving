def pentagonal_or_not(num):
    p = (1 + (1 + 24*num)**0.5) / 6
    return p.is_integer()

def hexagonal(num):
    h = (1 + (1 + 8*num)**0.5) / 4
    return h.is_integer()

the_num = 285
while True:
    triangle = the_num * (the_num + 1) // 2
    if pentagonal_or_not(triangle) and hexagonal(triangle):
        print(triangle)
        break
    the_num += 1