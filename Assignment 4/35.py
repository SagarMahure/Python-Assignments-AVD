n = int(input("Enter a number "))

f = 0
s = 1

print(f"{0} {1}",end=" ")
for i in range(3,n+1):
    th = f + s
    f = s
    s = th
    print(th,end=" ")