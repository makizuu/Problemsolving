def horizontal_lines(size):
    print(" ---" * size)

def vertical_lines(size):
    print("|   " * (size + 1))

def draw_grid(size):
    for _ in range(size):
        horizontal_lines(size)
        vertical_lines(size)
    horizontal_lines(size)

#for testing
a = 2
b = 4
draw_grid(a)
draw_grid(b)
