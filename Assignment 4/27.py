for i in range(1, 6):           # 5 rows
    for j in range(1, i + 1):   # j controls how many numbers per row
        print(j * 2, end=" ")   # print even number
    print()                     # new line after each row
