import random

def randomize_word():
    #opens the sowpods.txt file and reads all lines into a list
    with open('sowpods.txt', 'r') as f:
        words = f.readlines()
    
    #takes away newlines
    words = [word.strip() for word in words]
    
    #picks a random word from the list
    return random.choice(words)

def hangman():
    print("Welcome to Hangman!!")
    
    the_word = randomize_word()
    guessed = "_" * len(the_word)
    guessed = list(guessed)
    lstGuessed = []
    i = 6
    
    while i > 0:
        print("Current word: " + " ".join(guessed))
        print("You have " + str(i) + " incorrect guesses left.")
        
        letter = input("Guess a letter: ").upper()
        
        if letter in lstGuessed:
            print("Already guessed!!")
        elif letter in the_word:
            for index, char in enumerate(the_word):
                if char == letter:
                    guessed[index] = letter
            print("Correct!")
        else:
            i -= 1
            print("Incorrect!")
        
        if letter not in lstGuessed:
            lstGuessed.append(letter)

        if "_" not in guessed:
            print("Congratulations! You've guessed the word: " + ''.join(guessed))
            break
    else:
        print("Sorry, you've run out of guesses. The word was: " + the_word)
    
    if input("Do you want to play again? (yes/no): ").lower().startswith("y"):
        hangman()

if __name__ == "__main__":
    hangman()
