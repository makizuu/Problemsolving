def palindrome_base10(num):
    return str(num) == str(num)[::-1]

def palindrome_base2(num):
    bnum = bin(num)[2:]
    return bnum == bnum[::-1]

palindromic_nums = 0

for num in range(1,1000000):
    if palindrome_base10(num) and palindrome_base2(num):
        palindromic_nums += num

print(palindromic_nums)