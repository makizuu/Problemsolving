def count_divisors(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            count += 2
    if int(num**0.5) * int(num**0.5) == num:
        count -= 1
    return count

def triangle_number_with_over_x_divisors(x):
    num = 1
    triangle = 1
    while count_divisors(triangle) <= x:
        num += 1
        triangle += num

    return triangle

x = 500
print(triangle_number_with_over_x_divisors(x))