def fibonacci():
    num = int(input("How many Fibonnaci numbers to generate: "))
    i = 1

    if num == 0:
        list = []

    elif num == 1:
        list = [1]

    elif num == 2:
        list = [1,1]

    elif num > 2:
        list = [1,1]
        while i < (num - 1):
            list.append(list[i] + list[i-1])
            i += 1
    return list

def print_list(list):
    print(*list)
    return

print_list(fibonacci())