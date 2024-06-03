import json

def get_birthdays(json_file):
    try:
        with open(json_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_birthdays(json_file, dictionary):
    with open(json_file, 'w') as f:
        json.dump(dictionary, f, indent=4)

def main():
    filename = 'birthdays.json'
    the_dictionary = get_birthdays(filename)
    
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for name in the_dictionary:
        print(name)
    
    name = input("Who's birthday do you want to look up? ")
    
    birthday = the_dictionary.get(name)
    if birthday:
        print("" + name + "'s birthday is " + birthday)
    else:
        print("Sorry, we don't have the birthday information for " + name)
    
    new = input("Do you want to add a new birthday to the dictionary? (yes/no) ")
    if new.lower() == "yes":
        new_name = input("Enter the name: ")
        new_birthday = input("Enter the birthday (dd/mm/yyyy): ")
        the_dictionary[new_name] = new_birthday
        save_birthdays(filename, the_dictionary)
        print("Added " + new_name + "'s birthday to the dictionary.")

if __name__ == "__main__":
    main()
