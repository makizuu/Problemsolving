def greatest_common_divisor(a,b):
    while b:
        a,b = b,a % b
    return a

the_num = 1
the_den = 1

for num in range(10,100):
    for den in range(num + 1,100):
        numerator = str(num)
        denominator = str(den)
        common = None

        if numerator[0] in denominator:
            common = numerator[0]
        elif numerator[1] in denominator and numerator[1] != "0":
            common = numerator[1]

        if common:
            num2 = int(numerator.replace(common, '', 1))
            den2 = int(denominator.replace(common, '', 1))

            if den2 != 0 and num * den2 == den * num2:
                the_num *= num
                the_den *= den

gcd_product = greatest_common_divisor(the_num,the_den)
frank = the_den // gcd_product
print(frank)