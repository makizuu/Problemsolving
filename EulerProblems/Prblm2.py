def fibonacci_even_sum(max):
    a, b = 1, 2
    sum = 0
    
    while a <= max:
        if a % 2 == 0:
            sum += a

        a, b = b, a + b  
    return sum

print(fibonacci_even_sum(4000000))
