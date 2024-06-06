def prime_or_not(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def truncatable_or_not(num):
    snum = str(num)
    for i in range(1,len(snum)):
        if not prime_or_not(int(snum[i:])) or not prime_or_not(int(snum[:i])):
            return False
    return True

the_truncatables = []
num = 10

while len(the_truncatables) < 11:
    if prime_or_not(num) and truncatable_or_not(num):
        the_truncatables.append(num)
    num += 1

print(sum(the_truncatables))