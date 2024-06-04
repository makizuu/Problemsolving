power = 2 ** 1000
digits_sum = 0

for digit in str(power):
    digits_sum += int(digit)

print(digits_sum)