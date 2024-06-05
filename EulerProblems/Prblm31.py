two_pounds = 200
coins = [1,2,5,10,20,50,100,200]
ways = [0] * (two_pounds + 1)
ways[0] = 1

for c in coins:
    for i in range(c, two_pounds + 1):
        ways[i] += ways[i - c]

print(ways[two_pounds])