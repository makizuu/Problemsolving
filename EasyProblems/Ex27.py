def draw_board(board):
    print("game = [", end="")
    for i, row in enumerate(board):
        if i == 0:
            print(str(row) + ",")
        else:
            print("        " + str(row) + ",")
    print("        ]")

def get_play(player):
    while True:
        a = input("Player " + player + ", enter your move (row,col): ")
        try:
            row, col = map(int, a.split(","))
            if row in [1, 2, 3] and col in [1, 2, 3]:
                return row - 1, col - 1
            else:
                print("Invalid input, 1-3 numbers only")
        except ValueError:
            print("Invalid input, numbers should be separated by a comma")

def check_if_empty(board, row, col):
    return board[row][col] == 0

def update_board(board, row, col, player):
    board[row][col] = player

def main():
    the_board = [[0 for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    i = 0

    draw_board(the_board)

    while True:
        player = players[i % 2]
        row, col = get_play(player)

        if check_if_empty(the_board, row, col):
            update_board(the_board, row, col, player)
            i += 1
        else:
            print("That cell is not available! Try again.")

        draw_board(the_board)

        if i == 9:
            print("That's it")
            draw_board(the_board)
            break

if __name__ == "__main__":
    main()
