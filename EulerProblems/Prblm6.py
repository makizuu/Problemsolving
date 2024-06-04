squares_sum = sum([x**2 for x in range(1,101)])
sum_of_numbers = sum(range(1,101))
square_of_sum = sum_of_numbers ** 2

the_num = square_of_sum - squares_sum

print(the_num)