#checks if input is prime number
def is_prime():
    num = int(input("Give me a number: "))
    for i in range(2, num-1):
        if ((num/i) % 1) == 0:
            return "Your number is NOT prime number"
        break
    return "Your number is prime number"

print(is_prime())