def product_of_pos_ints(num):
    if num == 0:
        return 1
    else:
        return num*product_of_pos_ints(num-1)
    
the_num = 100
the_sum = sum(int(i) for i in str(product_of_pos_ints(the_num)))

print(the_sum)