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

def permutations(a, b, c):
    return sorted(str(a)) == sorted(str(b)) == sorted(str(c))

def find_sequence():
    for i in range(1000, 10000):
        if prime_or_not(i):
            for j in range(i + 1, 10000):
                if prime_or_not(j):
                    k = j + 3330
                    if k < 10000 and prime_or_not(k):
                        if permutations(i, j, k):
                            return str(i) + str(j) + str(k)

print(find_sequence())
