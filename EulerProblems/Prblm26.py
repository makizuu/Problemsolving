def recurring_cyclelength(num):
    list_a = []
    a = 1 % num

    while a not in list_a:
        list_a.append(a)
        a = (a * 10) % num

    return len(list_a) - list_a.index(a)

longest = 0
value_d = 0

for d in range(2, 1000):
    cyclelength = recurring_cyclelength(d)
    if cyclelength > longest:
        longest = cyclelength
        value_d = d

print(value_d)