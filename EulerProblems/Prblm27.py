def prime_or_not(num):
    if num < 2:
        return False
    for i in range(2, int(num** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def consecutive_prime_nums(a,b):
    n = 0
    while prime_or_not(abs(n**2 + a*n + b)):
        n += 1
    return n

max = 0
product = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        if prime_or_not(abs(b)):
            num_primes = consecutive_prime_nums(a,b)
            if num_primes > max:
                max = num_primes
                product = a * b

print(product)