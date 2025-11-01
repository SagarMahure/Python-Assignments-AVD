# leap year condition : 
# 4 should be divisible --> leap year
# 100 is divisible - -> Not a leap year except for year which are divisible by 400

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
