p = 0
n = 0
for i in range(1,11):
    k = int(input("Enter a number : "))
    if k>=0:
        p+=1
    else:
        n+=1

print(f"Positive number count : {p}\nnegative number count : {n}")