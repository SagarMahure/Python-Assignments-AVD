# Programm to calculate compound intrest

# Take input from user
P = float(input("Enter Principal amount (P): "))
R = float(input("Enter Rate of interest per annum (R): "))
T = float(input("Enter Time in years (T): "))

# Calculate final amount and compound interest
A = P * (1 + R / 100) ** T
CI = A - P

print(f"Final Amount after {T} years is: {A:.2f}")
print(f"Compound Interest is: {CI:.2f}")

