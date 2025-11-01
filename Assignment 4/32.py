n = int(input("Enter a number : "))
c = n
rev = 0

while n>0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10

if rev == c:
    print("Palindrome")
else:
    print("Not a Palindrome")