n = int(input("Enter a no : "))
rev = 0

while n>0:
    d = n % 10
    rev = rev * 10 + d    # Mathematics
    n = n // 10

print(rev)
