a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

def root(a,b,c):
    root1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
    root2 = (-b - (b**2-4*a*c)**0.5)/(2*a)

    print (f"Roots are {root1} and {root2}")
