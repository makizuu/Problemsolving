def sieve_of_eratosthenes(limit):
    prime_list = []
    prime_or_not = [True] * limit
    prime_or_not[0] = prime_or_not[1] = False

    for num in range(2, int(limit ** 0.5) + 1):
        if prime_or_not[num]:
            prime_list.append(num)
            for multiple in range(num * num, limit, num):
                prime_or_not[multiple] = False

    for num in range(int(limit ** 0.5) + 1, limit):
        if prime_or_not[num]:
            prime_list.append(num)

    return sum(prime_list)

the_num = 2000000
print(sieve_of_eratosthenes(the_num))