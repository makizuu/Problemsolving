def largest_num(var1, var2, var3):
    largest = 0
    if var1 > var2 and var1 > var3:
        largest = var1
    elif var2 > var1 and var2 > var3:
        largest = var2
    elif var3 > var1 and var3 > var2:
        largest = var3
    else:
        largest = 0
    return largest

def main():
    num1 = int(input("Give me the first number: "))
    num2 = int(input("Give me the second number: "))
    num3 = int(input("Give me the third and final number: "))

    if largest_num(num1,num2,num3) == 0:
        print("There are two of the same numbers")
        
    else:
        print("Largest of these numbers is " + str(largest_num(num1,num2,num3)))

if __name__ == "__main__":
    main()