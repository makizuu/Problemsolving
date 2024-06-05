from itertools import permutations

products = set()

for perm in permutations("123456789"):
    perm2 = ''.join(perm)
    for i in range(1, len(perm2)):
        for j in range(i + 1, len(perm2)):
            multiplicand = int(perm2[:i])
            multiplier = int(perm2[i:j])
            product = int(perm2[j:])
            if multiplicand * multiplier == product:
                products.add(product)

print(sum(products))