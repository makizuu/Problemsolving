#asks for a number and then prints out a list of all the divisors of that number
nro = int(input("Give me a number: "))
empty_list = []
for num in list(range(1,nro+1)):
    if num % nro == 0:
        empty_list.append(num)

print([num for num in range(1, nro+1) if nro % num == 0])