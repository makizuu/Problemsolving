import itertools

permutations = list(itertools.permutations("0123456789"))

millionth = ''.join(permutations[999999])

print(millionth)