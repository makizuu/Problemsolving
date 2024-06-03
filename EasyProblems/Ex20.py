#decides whether or not the given number is inside the list and returns an appropriate boolean
def search(list, number):
    left, right = 0, len(list) - 1

    while left <= right:
        i = (left + right) // 2
        num = list[i]

        if num == number:
            return True
        elif num < number:
            left = i + 1
        else:
            right = i - 1

    return False

the_list = [1, 3, 5, 7, 9, 11, 13, 15]

the_num = 7
answer = search(the_list, the_num)
print(answer)

the_num = 4
answer = search(the_list, the_num)
print(answer)
