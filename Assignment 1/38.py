n = int(input("Enter a number"))
temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    print(digit)
    sum = sum + digit
    temp = temp // 10

print(f"The total sum is {sum}")


