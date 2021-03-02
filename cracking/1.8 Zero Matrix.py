#Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
#column are set to 0,

matrix = [[1,2,3],
          [4,5,0],
          [0,8,9]]

row = len(matrix)
col = len(matrix[0])
row_s = []
col_s = []
print("Before:")
for i in matrix:
    print(i)
for i in range(row):
    if i in row_s:
        continue
    for j in range(col):
        if j in col_s:
            continue
        if matrix[i][j] == 0:
            if j not in col_s:
                col_s.append(j)
            if i not in row_s:
                row_s.append(i)
for i in row_s:
    for j in range(col):
        matrix[i][j] = 0
for i in col_s:
    for j in range(row):
        matrix[j][i] = 0

print("After:")
for i in matrix:
    print(i)