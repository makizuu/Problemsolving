def is_abu(n):
    divisors_sum = sum(i for i in range(1, n//2 + 1) if n % i == 0)
    return divisors_sum > n

abundant_nums = [i for i in range(12, 28123) if is_abu(i)]

sum_two_abu = set()
for a in abundant_nums:
    for b in abundant_nums:
        if a + b <= 28123:
            sum_two_abu.add(a + b)

the_print = sum(i for i in range(1, 28123) if i not in sum_two_abu)

print(the_print)