import math

def pentagonal_or_not(num):
    p = (1 + math.sqrt(1 + 24*num)) / 6
    return p.is_integer()

max = 10000
pentagonals = [num*(3*num-1)//2 for num in range(1, max)]

D = float('inf')
for k in range(len(pentagonals)):
    for j in range(k+1, len(pentagonals)):
        if pentagonal_or_not(pentagonals[j] - pentagonals[k]) and pentagonal_or_not(pentagonals[j] + pentagonals[k]):
            if pentagonals[j] - pentagonals[k] < D:
                D = pentagonals[j] - pentagonals[k]

print(D)