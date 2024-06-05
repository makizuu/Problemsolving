def sum_amicable_nums_under_10000(num):
    return sum([i for i in range(1, num) if num % i == 0])

amicable_nums = set()
for a in range (2,10000):
    b = sum_amicable_nums_under_10000(a)
    if a != b and sum_amicable_nums_under_10000(b) == a:
        amicable_nums.add(a)
        amicable_nums.add(b)

print(sum(amicable_nums))