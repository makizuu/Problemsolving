def horizontal_lines(size):
    print(" ---" * size)

def vertical_lines(size, board, row):
    line = "|"
    for col in range(size):
        if board[row][col] == 0:
            line += "   |"
        else:
            line += " " + board[row][col] + " |"
    print(line)

def draw_board(board):
    size = len(board)
    for row in range(size):
        horizontal_lines(size)
        vertical_lines(size, board, row)
    horizontal_lines(size)

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

def winner_is(board):
    #checks rows for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != 0:
            return row[0]
    
    #checks columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return board[0][col]
    
    #checks diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    
    #no winner
    return None

def main():
    play_again = True
    scores = {"X": 0, "O": 0}
    
    while play_again:
        board = [[0 for _ in range(3)] for _ in range(3)]
        players = ["X", "O"]
        i = 0
        draw_board(board)
        
        while True:
            player = players[i % 2]
            row, col = get_play(player)

            if check_if_empty(board, row, col):
                update_board(board, row, col, player)
                i += 1
            else:
                print("That cell is not available! Try again.")
                continue

            draw_board(board)

            winner = winner_is(board)
            if winner:
                print("Congratulations! Player " + winner + " wins!")
                scores[winner] += 1
                break

            if i == 9:
                print("It's a draw!")
                break

        print("Scoreboard: Player X - {0}, Player O - {1}".format(scores["X"], scores["O"]))
        play_again = input("Do you want to play again? (yes/no): ").strip().lower() == "yes"

if __name__ == "__main__":
    main()
