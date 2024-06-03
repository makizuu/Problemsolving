import json

def get_birthdays(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def main():
    the_dictionary = get_birthdays('birthdays.json')
    
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for name in the_dictionary:
        print(name)
    
    name = input("Who's birthday do you want to look up? ")
    
    birthday = the_dictionary.get(name)
    if birthday:
        print("" + name + "'s birthday is " + birthday)
    else:
        print("Sorry, we don't have the birthday information for " + name)

if __name__ == "__main__":
    main()
