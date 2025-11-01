n = int(input("Enter a number"))
c = 0
for i in range(2,int(n**0.5)):
    if n%i == 0:
        c+=1
    
if c==0:
    print("Prime Number")
else:
    print("Not a Prime Number")