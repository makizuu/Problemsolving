def sum_fifth_powers(num):
    return sum(int(digit)**5 for digit in str(num))

result = 0
for the_num in range(2, 1000000):
    if the_num == sum_fifth_powers(the_num):
        result += the_num

print(result)