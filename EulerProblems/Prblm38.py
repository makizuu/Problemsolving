def pandigital_or_not(num):
    return sorted(str(num)) == ['1','2','3','4','5','6','7','8','9']

def concatenated_product(num):
    result = ''
    a = 1
    while len(result) < 9:
        result += str(num * a)
        a += 1
    return int(result)

largest = 0

for i in range(1,10000):
    product = concatenated_product(i)
    if len(str(product)) == 9 and pandigital_or_not(product):
        largest = max(largest, product)

print(largest)