def largest_dividor(a,b):
    while b:
        a,b = b,a % b
    return a

def smallest_divisible(a,b):
    return a*b // largest_dividor(a,b)

def the_range(num):
    answer = 1
    for i in range(2, num +1):
        answer = smallest_divisible(answer, i)
    return answer

the_num = the_range(20)
print (the_num)