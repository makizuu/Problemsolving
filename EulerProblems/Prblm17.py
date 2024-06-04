def number_to_words(num):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
            "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if num == 1000:
        return "onethousand"
    elif num >= 100:
        if num % 100 == 0:
            return ones[num // 100] + "hundred"
        else:
            return ones[num // 100] + "hundredand" + number_to_words(num % 100)
    elif num >= 20:
        return tens[num // 10] + ones[num % 10]
    else:
        return ones[num]
    
all_letters = 0

for i in range(1,1001):
    all_letters += len(number_to_words(i))

print(all_letters)