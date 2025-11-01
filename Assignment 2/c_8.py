ch = input("Enter a single character: ")

if len(ch) == 1 and (('A' <= ch <= 'Z') or ('a' <= ch <= 'z')):
    print("Alphabet")
else:
    print("Not an alphabet")