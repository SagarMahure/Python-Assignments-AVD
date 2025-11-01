n = input("Enter a character : ").lower()

if n.isalpha() and len(n) == 1:
    if n in "aeiou":
        print("vovel")
    else:
        print("consonant")

else:
    print("Enter a valid character")