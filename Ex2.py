num = int(input("Give a number: "))
check = int(input("Give a number to divide with: "))
y = num % 2
if num % check == 0:
    print("First number is evenly dividable by the other number")
elif num % 4 == 0:
    print("First number is a multiple of 4")
elif y == 0:
    print("First number is an even number")
else:
    print("First number is an odd number")