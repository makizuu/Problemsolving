segment = ''.join(str(i) for i in range(1, 1000000))
value = 1

for power in range(7):
    i = 10**power
    num = int(segment[i - 1])
    value *= num

print(value)