import random

the_num = random.randrange(1, 10)
num = 0
i = 0

#Number guessing game that ends when you get it right or write exit

while num != the_num and num != "exit":

    num = input("Guess a number (between 1-9): ")

    if num == "exit":
        break

    num = int(num)
    i += 1

    if num > the_num:
        print("Too high")

    elif num < the_num:
        print("Too low")

    else:
        print("Exactly right")
        print("You took total of", i, "guesses")