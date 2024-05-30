#gives the user given string in backwards order
def reverse(phrase):
    words = phrase.split()
    words.reverse()
    return ' '.join(words)

a = input("Give me a phrase: ")
print(reverse(a))