import random

def randomize_word():
    #opens the sowpods.txt file and reads all lines into a list
    with open('sowpods.txt', 'r') as f:
        words = f.readlines()
    
    #takes away newlines
    words = [word.strip() for word in words]
    
    #picks a random word from the list
    the_word = random.choice(words)
    
    return the_word

if __name__ == "__main__":
    print(randomize_word()) #for testing
