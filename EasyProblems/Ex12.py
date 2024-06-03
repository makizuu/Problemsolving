import random

#returns the first and last elements on a list
def first_and_last(list):
    return [list[0], list[-1]]

#prints list
def print_list(list):
    print(*list)
    return

a = [5, 10, 15, 20, 25]
b = random.sample(range(1,100), 10)

print_list(a)
print_list(b)

print(first_and_last(a))
print(first_and_last(b))