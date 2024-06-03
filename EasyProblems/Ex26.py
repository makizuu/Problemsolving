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

#test cases
winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]

print(winner_is(winner_is_2))
print(winner_is(winner_is_1))
print(winner_is(winner_is_also_1))
print(winner_is(no_winner))
print(winner_is(also_no_winner))
