from birthdays import birthdays_dictionary

def main():
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for name in birthdays_dictionary:
        print(name)
    
    name = input("Who's birthday do you want to look up? ")
    
    birthday = birthdays_dictionary.get(name)
    if birthday:
        print("" + name + "'s birthday is " + birthday)
    else:
        print("Sorry, we don't have the birthday information for " + name)

if __name__ == "__main__":
    main()
