def check_palindrome(num):
    return str(num) == str(num)[::-1]

largest = 0

for i in range(100,1000):
    for j in range(100,1000):
        product = i *  j
        if check_palindrome(product) and product > largest:
            largest = product

print(largest)