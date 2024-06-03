import datetime

name = input("Give me your name: ")
age = int(input("How old you are/ you'll be this year: "))

now = datetime.datetime.now()
year = now.year - age + 100

print(f"Hello {name}, you will bee 100 years old in {year}")