n = int(input("Enter a number"))

def isArg(num):
    len = 0
    temp = num
    sum = 0
    while temp>0:
        len = len + 1
        temp = temp // 10
        
    temp = num    
    
    while temp>0:
        digit = temp % 10
        sum = sum + digit ** len
        temp = temp // 10

    if sum == num:
        print("yes")
    else:
        print("No")

isArg(n)


       