num = 1000
for a in range (1,num):
    for b in range(a,num):
        c = num - a - b
        if a ** 2 + b ** 2 == c ** 2:
            abc = a * b * c
            print(f"{a} + {b} + {c} = {num}, and the product abc = {abc}")
            break