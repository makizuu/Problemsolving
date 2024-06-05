def diagonals_sum_spiral(size):
    if size % 2 == 0:
        return "Odd nums only"
    
    total = 1
    current_num = 1
    for i in range(3, size + 1,2):
        for _ in range(3):
            current_num += i - 1
            total += current_num

    return total

spiral_size = 1001
print(diagonals_sum_spiral(spiral_size))