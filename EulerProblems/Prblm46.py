def prime_or_not(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def goldbach_conjecture(num):
    for i in range(1, int((num/2)**0.5) + 1):
        if prime_or_not(num - 2*i*i):
            return True
    return False

odd_num = 9
while True:
    if not prime_or_not(odd_num) and not goldbach_conjecture(odd_num):
        print(odd_num)
        break
    odd_num += 2