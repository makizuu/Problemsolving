import math

def prime_or_not(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_pandigital_nums(a, b, c):
    if not b:
        num = int(a)
        if prime_or_not(num):
            c.append(num)
    for i in b:
        generate_pandigital_nums(a + i, b.replace(i, ''), c)

pandigital_primes = []
generate_pandigital_nums('', '7654321', pandigital_primes)

largest = max(pandigital_primes)

print(largest)