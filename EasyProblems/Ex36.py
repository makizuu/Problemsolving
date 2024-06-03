import json
from collections import defaultdict, OrderedDict
from bokeh.plotting import figure, show, output_file

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
        ordered_month_count[m] = count[m]
    
    return ordered_month_count

#takes the month count dictionary and plots a histogram using Bokeh
def histogram_make(count):
    months = list(count.keys())
    counts = list(count.values())

    p = figure(x_range=months, height=250, title="Birthday counts by month",
               toolbar_location=None, tools="")
    p.vbar(x=months, top=counts, width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    output_file("birthdays_histogram.html")
    show(p)

def main():
    filename = 'birthdays.json'
    the_dictionary = get_birthdays(filename)
    
    count = month_count(the_dictionary)
    
    histogram_make(count)

if __name__ == "__main__":
    main()
