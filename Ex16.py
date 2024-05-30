import random
#generates weak passwords with two words
def weaks():
    a = ["fish", "apple", "dog", "sea", "tree", "house", "red", "plant", "qwerty"]
    b = ''.join(random.sample(a, 2))
    return b

#generates strong passwords that include 8-12 characters that are lowercase and uppercase letters, numbers and symbols
def strongs():
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    password = [random.choice(lowercase), random.choice(uppercase), random.choice(numbers), random.choice(symbols)]
    all = lowercase + uppercase + numbers + symbols
    length = random.randint(8, 12)
    password  += random.choices(all, k=length - 4)

    random.shuffle(password)
    password = ''.join(password)

    return password

def main():
    spice = input("How strong of a password you want? (weak or strong): ")

    if spice == "weak":
        print("Your weak password is: " + weaks())
    elif spice == "strong":
        print("Your strong password is: " + strongs())
    else:
        print("Wrong input")

if __name__ == "__main__":
    main()
