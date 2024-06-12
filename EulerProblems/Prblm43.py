def isit_divisible(num):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        if int(num[i:i+3]) % primes[i-1] != 0:
            return False
    return True

def generate_permutations(nums, max, min):
    if min == max:
        num = ''.join(nums)
        if isit_divisible(num):
            return int(num)
        return 0
    else:
        all_pans = 0
        for i in range(min, max):
            nums[min], nums[i] = nums[i], nums[min]
            all_pans += generate_permutations(nums, max, min + 1)
            nums[min], nums[i] = nums[i], nums[min]
        return all_pans

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
all_pans = generate_permutations(nums, 10, 0)

print(all_pans)