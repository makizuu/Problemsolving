def series_last_ten():
    total = 0
    for i in range(0, 1000):
        total += i ** i
    last_ten_digits = total % (10 ** 10)
    return last_ten_digits

print(series_last_ten())
