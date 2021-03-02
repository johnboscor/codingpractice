#https://www.interviewbit.com/problems/zigzag-string/
A = "PAYPALISHIRING"
row = 3

A = "ABCD"
row = 2

A = "ABCDEFGHIJKLMNOPQRS"
row = 6
#output:
#P.......A........H.......N
#..A..P....L....S....I...I....G
#....Y.........I........R
#PAHNAPLSIIGYIR

#0 1 2 1 0 1 2 1 0
if row == 1:
    print(A)
res = [""] * row
col = 0
add = True
for i in range(len(A)):
    if col == 0:
        add = True
    elif col == row-1:
        add = False
    res[col] += A[i]
    if add:
        col += 1
    else:
        col -=1

print(''.join(res))