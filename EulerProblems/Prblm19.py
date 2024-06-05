import datetime

start = datetime.date(1901,1,1)
end = datetime.date(2000,12,31)

sundays = 0

while start <= end:
    if start.day == 1 and start.weekday() == 6:
        sundays += 1
    start += datetime.timedelta(days=1)

print(sundays)