def words_to_ints(word):
    return sum(ord(letter) - ord('A') + 1 for letter in word)

triangle_nums = [n * (n + 1) // 2 for n in range(1, 30)]

with open('words.txt', 'r') as file:
    words = file.read().replace('"', '').split(',')

triangle_words = sum(words_to_ints(word) in triangle_nums for word in words)

print(triangle_words)