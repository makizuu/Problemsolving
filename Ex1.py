import datetime
"""age = input("Enter your age: ")
age = int(age)"""
name = input("Give me your name: ")
age = int(input("How old you are/ you'll be this year: "))

#getting today's year
now = datetime.datetime.now()
year = now.year - age + 100

print("Hello " + name + ", you will bee 100 years old in " + str(year))