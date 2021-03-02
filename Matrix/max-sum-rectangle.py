#https://www.youtube.com/watch?v=-FgseNO-6Gk

A = [-5,3,1,-1,4,6]

def kadane(A):
    max_sum = float('-inf')
    curr_sum = 0
    max_start = start = end = 0
    for i in range(len(A)):
        if curr_sum <= 0:
            curr_sum = A[i]
            start = i
        else:
            curr_sum += A[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_start = start
            end = i
    return(max_sum,max_start,end)
print(kadane(A))

arr = [[6,-5,-7, 4],
       [-9,3,-6,5,2],
       [-10,4,7,-6,3],
       [-8,9,-3,3,7]]
row_len = len(arr)
col_len = len(arr[0])

left = right = 0
max_left = 0
max_right = 0
max_top = 0
max_bottom = 0
max_sum = float('-inf')
while True:
    curr_sum = curr_top = curr_bottom = 0
    sub_sum = []
    for j in range(row_len):
        sub_sum.append(sum(arr[j][left:right+1]))
    #print(sub_sum)
    curr_sum, curr_top, curr_bottom = kadane(sub_sum)
    #print(curr_sum, curr_top, curr_bottom)
    if curr_sum > max_sum:
        max_sum = curr_sum
        max_left = left
        max_right = right
        max_top = curr_top
        max_bottom = curr_bottom
    right += 1
    if right >= col_len:
        left += 1
        right = left
    if left >= col_len:
        break

print(max_sum, max_left, max_right, max_top, max_bottom)