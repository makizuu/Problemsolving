#The user will have in their head a number between 0 and 100. The user will say whether programs guess is too high, too low, or your number.
def right_or_wrong(guess):
    return input("My guess is " + str(guess) + ". Is it too low, too high, or correct? ").lower()

#Calculates the new midpoint
def midpoint(low, high):
    return (low + high) // 2

#The program will guess a number
def guess_number():
    low = 0
    high = 100
    guess = midpoint(low, high)
    i = 1

    print("Think of a number between 0 and 100, and I will try to guess it.")

    while True:
        a = right_or_wrong(guess)

        if a == "correct":
            print("I guessed the number " + str(guess) + " in " + str(i) + " guesses.")
            break
        elif a == "too low":
            low = guess + 1
        elif a == "too high":
            high = guess - 1
        else:
            print("Please respond with 'too low', 'too high', or 'correct'.")
            continue

        guess = midpoint(low, high)
        i += 1

if __name__ == "__main__":
    guess_number()
