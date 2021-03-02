#https://www.interviewbit.com/problems/set-matrix-zeros/

A = [[1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 0 ,1 ] ]
print(A)
row_len = len(A)
col_len = len(A[0])

temp = []
for row in range(row_len):
    for col in range(col_len):
        if A[row][col] == 0:
            temp.append([row,col])

for i in temp:
    for r in range(col_len):
        A[i[0]][r] = 0
    for c in range(row_len):
        A[c][i[1]] = 0

print(A)

