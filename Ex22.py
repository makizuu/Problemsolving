#counts how many of each name there are in the file, and print out the results
def namecount(file_name):
    with open(file_name, 'r') as f:
        names = f.read().splitlines()

    name_counts = {}

    for i in names:
        if i in name_counts:
            name_counts[i] += 1
        else:
            name_counts[i] = 1

    for i, count in name_counts.items():
        print("{}: {}".format(i, count))

the_file = input("Give me the file with .txt extension that has the list of names: ")

namecount(the_file)
