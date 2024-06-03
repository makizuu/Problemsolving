num = int(input("Give a number: "))
check = int(input("Give a number to divide with: "))
y = num % 2

if num % check == 0:
    print(num, "is evenly dividable by", check)
elif num % 4 == 0:
    print(num, "is a multiple of 4")
elif y == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")