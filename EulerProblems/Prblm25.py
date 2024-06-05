def fib_nums(nums):
    a, b = 1,1
    index = 2
    while len(str(b)) < nums:
        a,b = b, a + b
        index += 1

    return index

digits = 1000
print(fib_nums(digits))