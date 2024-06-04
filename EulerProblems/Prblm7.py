def prime_or_not(num):
    if num < 2:
        return False
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_the_prime(the_num):
    num = 2
    while True:
        if prime_or_not(num):
            the_num -= 1
            if the_num == 0:
                return num
        num += 1

print(find_the_prime(10001))