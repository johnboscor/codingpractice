#Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
#bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

N = len(matrix)

print("Before:")
for i in matrix:
    print(i)
i = j = 0
for k in range(N):
    for i in range(j,N):
        matrix[i][k], matrix[k][i] = matrix[k][i], matrix[i][k]
    j += 1
print("After:")
for i in matrix:
    print(i)