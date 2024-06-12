def prime_divisors(num):
    divisors = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            divisors.add(i)
    if num > 1:
        divisors.add(num)
    return divisors

def four_or_not(num):
    return len(prime_divisors(num)) == 4

prime = 2
i = 0

while i < 4:
    if four_or_not(prime):
        i += 1
    else:
        i = 0
    prime += 1

first_num = prime - 4

print(first_num)
