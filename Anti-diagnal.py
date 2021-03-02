A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

'''
#O(n*n) complexity... not good
res = []
n = len(A)
d = {}
for i in range(2 * n - 1):
    d[i] = []
iter = 0
for i in range(n):
    for j in range(n):
        if i + j in d:
            l = d[i + j]
            l.append(A[i][j])
            iter += 1

print(list(d.values()))
print(f"No. of iterations = {iter}")
'''

# My solution
row_len = len(A)
col_len = len(A[0])
for i in A:
    print(i)


B = []
start_row = 0
start_col = 0
while True:
    C = []

    j = 0
    curr_row = start_row
    for j in range(start_col, col_len):
        C.append(A[j][curr_row])
        if curr_row == 0:
            break
        curr_row -= 1
    if C:
        B.append(C)

    if start_row < row_len - 1:
        start_row += 1
    else:
        start_col += 1

    if start_col > (col_len - 1):
        break
print(B)

