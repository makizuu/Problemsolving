def product_of_pos_ints(num):
    if num == 0:
        return 1
    else:
        return num * product_of_pos_ints(num-1)
    
def calculate_routes(num):
    routes = product_of_pos_ints(2*num) // (product_of_pos_ints(num) ** 2)
    return routes

size = 20
print(calculate_routes(size))