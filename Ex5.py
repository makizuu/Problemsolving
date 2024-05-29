"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

empty_list = []

print(a)
print(b)
print("")

for i in a:
    if i in b:
        empty_list.append(i)

print(empty_list)
"""
#finds common numbers in random number lists and prints them
import random

a = random.sample(range(1, 100), 10)
b = random.sample(range(1, 100), 15)

print(a)
print(b)
print(set([i for i in min(a,b) if i in max(a,b)]))
