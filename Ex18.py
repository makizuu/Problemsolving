import random

def cows(answer, guess):
    #For every digit that the user guessed correctly in the correct place, they have a “cow”
    cows_count = 0
    for a, g in zip(answer, guess):
        if a == g:
            cows_count += 1
    return cows_count

def bulls(answer, guess):
    #For every digit the user guessed correctly in the wrong place is a “bull.”
    bulls_count = 0
    answer_list = list(answer)
    guess_list = list(guess)

    for i in range(len(guess_list)):
        if guess_list[i] == answer_list[i]:
            answer_list[i] = guess_list[i] = None
    
    for x in guess_list:
        if x and x in answer_list:
            bulls_count += 1
            answer_list.remove(x)
    return bulls_count

def gameplay():
    print("Welcome to COWS & BULLS")
    the_num = random.randint(0, 9999)
    right = str(the_num).zfill(4)

    i = 0
    while True:    
        num = input("Guess a 4-digit number: ").zfill(4)
        i += 1
        #print(right) #for testing

        if len(num) != 4 or not num.isdigit():
            print("Invalid input!")
            continue

        if num == right:
            print("CONGRATULATIONS! You've guessed the correct number " + str(right) + " in " + str(i) + " guesses.")
            break

        cow_num = cows(right, num)
        bull_num = bulls(right, num)

        print(str(cow_num) + " cow(s), " + str(bull_num) + " bull(s)")

gameplay()