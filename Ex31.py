def hangman():
    print("Welcome to Hangman!!")
    the_word = "EVAPORATE"
    guessed = "_" * len(the_word)
    the_word = list(the_word)
    guessed = list(guessed)
    lstGuessed = []
    
    while True:
        letter = input("Guess a letter: ").upper()
        
        if letter in lstGuessed:
            print("Already guessed!!")
        elif letter in the_word:
            for index, char in enumerate(the_word):
                if char == letter:
                    guessed[index] = letter
                    the_word[index] = '_'
            print(''.join(guessed))
        else:
            print("Incorrect!")
            print(''.join(guessed))
        
        if letter not in lstGuessed:
            lstGuessed.append(letter)

        if "_" not in guessed:
            print("Congratulations! You've guessed the word: " + ''.join(guessed))
            break

if __name__ == "__main__":
    hangman()
