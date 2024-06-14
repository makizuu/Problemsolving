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
    a = [True] * (limit + 1)
    a[0] = a[1] = False  # 0 and 1 are not prime numbers
    for x in range(2, int(limit**0.5) + 1):
        if a[x]:
            for y in range(x * x, limit + 1, x):
                a[y] = False
    return [num for num, is_prime in enumerate(a) if is_prime]

def sum_consecutive_prime(primes):
    a = 0
    b = 0
    max = 1000000
    
    for i in range(len(primes)):
        for j in range(i + b, len(primes)):
            prime_sum = sum(primes[i:j])
            if prime_sum >= max:
                break
            if prime_or_not(prime_sum):
                current_length = j - i
                if current_length > b:
                    b = current_length
                    a = prime_sum
                    
    return a, b

max = 1000000
the_primes = primes_till(max)

print(sum_consecutive_prime(the_primes))
