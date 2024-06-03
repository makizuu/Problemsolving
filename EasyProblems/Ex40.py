import random

number = random.randint(1, 9)
number_of_guesses = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 9: "))
        if 1 <= guess <= 9:
            number_of_guesses += 1
            if guess == number:
                break
        else:
            print("Please enter a number between 1 and 9.")
    except ValueError:
        print("Please enter a valid number.")

print(f"You needed {number_of_guesses} guesses to guess the number {number}")
