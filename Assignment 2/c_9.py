n = int(input("Enter a number : "))
temp = n
count = 0

while temp > 0:
    count = count + 1
    temp = temp // 10

if count == 1:
    print("Single")
elif count == 2:
    print("Double")
elif count == 3:
    print("Triple")
else:
    print("Enter a number which having length 1,2 or 3")


    # Or

# n = int(input("Enter a number: "))

# if 0 <= n <= 9:
#     print("Single Digit")
# elif 10 <= n <= 99:
#     print("Double Digit")
# elif 100 <= n <= 999:
#     print("Triple Digit")
# else:
#     print("Enter a number with 1, 2, or 3 digits")

