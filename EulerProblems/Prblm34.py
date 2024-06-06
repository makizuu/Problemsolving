def product_of_pos_ints(num):
    if num == 0:
        return 1
    return num * product_of_pos_ints(num-1)

limit = product_of_pos_ints(9) * 7
total = 0

for num in range(10,limit):
    digit_sum = sum(product_of_pos_ints(int(digit)) for digit in str(num))
    if digit_sum == num:
        total += num

print(total)