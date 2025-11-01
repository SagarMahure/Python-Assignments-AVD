# Input: a three-digit number
num = int(input("Enter a 3-digit number: "))

# Extract digits
hundreds = num // 100
tens = (num % 100) // 10
units = num % 10

# Reverse the number
reversed_num = (units * 100) + (tens * 10) + hundreds

# Output
print(f"Reversed number is: {reversed_num}")
