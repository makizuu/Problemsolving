def multiples_sum(num):
    sum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(multiples_sum(1000))
