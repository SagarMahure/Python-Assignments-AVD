days = int(input("Enter total days : "))

years = days // 365
rem_days = years % 365

month = rem_days // 30
rem_days = month % 30

print(f"The total is {years} year, {month} month and {rem_days} days")