def sequence_length(num):
    count = 1
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        count += 1
    return count

max_chain_length = 0
starting_num = 0
max_starting_num = 1000000

for i in range(1, max_starting_num):
    length = sequence_length(i)
    if length > max_chain_length:
        max_chain_length = length
        starting_num = i

print(starting_num)