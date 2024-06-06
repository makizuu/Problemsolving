def prime_or_not(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_rotations(num):
    snum = str(num)
    rotations = [int(snum[i:] + snum[:i]) for i in range(len(snum))]
    return rotations

circular_primes = 0

for num in range(2,1000000):
    if all(prime_or_not(rotes) for rotes in generate_rotations(num)):
        circular_primes += 1

print(circular_primes)