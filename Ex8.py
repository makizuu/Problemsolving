print("ROCK PAPER SCISSORS")
while True:
    p1 = input("Player1 choose your play (rock, paper or scissors): ")
    p2 = input("Player2 choose your play (rock, paper or scissors): ")

    r = "rock"
    p = "paper"
    s = "scissors"

    #player1 wins in these cases: p1 r p2 s, p1 p p2 r, p1 s p2 p
    #player2 wins in these cases p2 r p1 s, p2 p p1 r, p2 s p1 p

    if p1 == p2:
        print("It's a tie!")

    elif p1 == r and p2 == s or p1 == p and p2 == r or p1 == s and p2 == p:
        print("Congratulations Player 1! You are the Winner!")

    elif p2 == r and p1 == s or p2 == p and p1 == r or p2 == s and p1 == p:
        print("Congratulations Player 2! You are the Winner!")

    else:
        print("Wrong input")
        continue

    quit = input("Do you want to start a new game (yes or no): ")
    if quit == "yes":
        continue
    elif quit == "no":
        break

    else:
        print("Wrong input")
        break
