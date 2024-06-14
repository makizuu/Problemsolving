from itertools import combinations

def prime_or_not(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def primes_till(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for x in range(2, int(limit**0.5) + 1):
        if a[x]:
            for y in range(x*x, limit, x):
                a[y] = False
    return [num for num, is_prime in enumerate(a) if is_prime]

def family_prime_small(size):
    primes = primes_till(1000000)
    for prime in primes:
        word = str(prime)
        word_length = len(word)
        for i in range(1, word_length):
            for digits in combinations(range(word_length), i):
                c = 0
                for digit in '0123456789':
                    candidate = list(word)
                    for d in digits:
                        candidate[d] = digit
                    candidate_str = ''.join(candidate)
                    if candidate_str[0] != '0' and prime_or_not(int(candidate_str)):
                        c += 1
                if c >= size:
                    return prime

print(family_prime_small(8))
