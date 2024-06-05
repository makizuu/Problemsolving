def name_score(name):
    return sum(ord(char) - 64 for char in name)

with open('names.txt', 'r') as file:
    names = sorted(file.read().replace('"','').split(','))

score = 0
for index, name in enumerate(names,start=1):
    n_score = name_score(name) * index
    score += n_score

print(score)