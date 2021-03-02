A = [[1, 3, 5, 7],  [10, 11, 16, 20],  [23, 30, 34, 50]]

B = 3
for i in A:
    if B in i:
        print("Found")
        break
    else:
        print("Not Found")