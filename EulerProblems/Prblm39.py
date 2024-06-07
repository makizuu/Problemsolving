def rightangled_triangle(a, b, c):
    return a**2 + b**2 == c**2

the_max = 0
maxp = 0

for p in range(1, 1001):
    solutions = 0
    for a in range(1, p//2):
        for b in range(1, p//2):
            c = p - a - b
            if a + b + c == p and rightangled_triangle(a, b, c):
                solutions += 1
    if solutions > the_max:
        the_max = solutions
        maxp = p

print(maxp)