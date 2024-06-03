"""a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#prints out all the elements of the list that are less than 5
for num in a:
    if num<5:
        print(num)"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []
y =[]

#prints out all the elements of the list that are less than 5
for num in a:
    if num < 5:
        x.append(num)
print(x)

#prints out all the elements of the list that are less than the number given by user
num = int(input("Enter a number: "))
for n in a:
    if n < num:
        y.append(n)
print(y)
