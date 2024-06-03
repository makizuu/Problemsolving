def largest_prime_factor(num):
    i = 2
    while i * i <= num:
        while num % i == 0:
            num //= i
        i += 1
    if num > 1:
        return num
    return i

the_num = 600851475143
print(largest_prime_factor(the_num))