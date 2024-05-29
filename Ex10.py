import random

a = random.sample(range(1, 100), 10)
b = random.sample(range(1, 100), 15)

print(set([i for i in min(a,b) if i in max(a,b)]))