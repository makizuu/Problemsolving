def horizontal_lines(size):
    print(" ---" * size)

def vertical_lines(size):
    print("|   " * (size + 1))

def draw_board(size):
    for _ in range(size):
        horizontal_lines(size)
        vertical_lines(size)
    horizontal_lines(size)

def main():
    size = int(input("What size game board you want to draw (for example 3 = 3X3): "))
    draw_board(size)

if __name__ == "__main__":
    main()
