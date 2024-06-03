def read_numbers(file_name):
    with open(file_name, 'r') as f:
        nums = f.read().split()
    return set(map(int, nums))

def find_overlaps(file1, file2):
    set1 = read_numbers(file1)
    set2 = read_numbers(file2)
    return set1.intersection(set2)

primenums = "primenumbers.txt"
happynums = "happynumbers.txt"

the_nums = find_overlaps(primenums, happynums)

print("Overlapping numbers:", the_nums)
