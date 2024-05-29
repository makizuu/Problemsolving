test_word = input("Give me a word: ")
palindrome = test_word[::-1]

if test_word == palindrome:
    print("The word " + test_word + " is a palindrome")
else:
    print("The word " + test_word + " is not a palindrome")