#https://www.geeksforgeeks.org/median/
# sum of left == sum of right

A = [ 1, 2, 3, 4, 5, 2, -1]
ln = len(A)
if ln <= 1:
    print('0')
if ln == 2:
    print('-1')

sum_arr = [A[0]]
for i in range(1,ln):
    sum_val = sum_arr[i-1] + A[i]
    sum_arr.append(sum_val)

found = False
for i in range(2,ln-1):

    sum_left = sum_arr[i] - A[i]
    sum_right = sum_arr[ln-1] - sum_arr[i]
    if sum_left == sum_right:
        found = True
        break
if found:
    print('0')
else:
    print('-1')