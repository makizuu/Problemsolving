#takes a list and returns a new list that contains all the elements of the first list minus all the duplicates
def minus_dupl(list):
    a = []
    for i in list:
        if i not in a:
            a.append(i)
        else:
            pass
    return a
    
a = [1,1,2,3,3,4,5,3,6,7]
print(minus_dupl(a))