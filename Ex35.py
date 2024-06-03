import json
from collections import defaultdict, OrderedDict

def get_birthdays(json_file):
    try:
        with open(json_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

#extracts the months of all the birthdays and counts how many birthdays in each month
def month_count(dictionary):
    count = defaultdict(int)
    months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]
    
    for b in dictionary.values():
        month_number = int(b.split('/')[1])
        month_name = months[month_number - 1]
        count[month_name] += 1

    ordered_month_count = OrderedDict()

    for m in months:
        if m in count:
            ordered_month_count[m] = count[m]
    
    return ordered_month_count

def main():
    filename = 'birthdays.json'
    the_dictionary = get_birthdays(filename)
    
    count = month_count(the_dictionary)
    
    print(json.dumps(count, indent=4))

if __name__ == "__main__":
    main()
