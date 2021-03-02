# return max of |A[i] - A[j]| + |i - j|
# assume position 0 is 1.

A = [1, 3, -1]

def maxArr_brute(A):
    max_val=0
    for i in range(len(A)):
        for j in range(i,len(A)):
            curr_val = abs(A[i] - A[j]) + abs((i+1) - (j+1))
            max_val = max(curr_val, max_val)

    return max_val

def maxArr_fast(array):
    max1 = -2147483648
    min1 = +2147483647
    max2 = -2147483648
    min2 = +2147483647

    for i in range(len(array)):
        # Updating max and min variables
        # as described in algorithm.
        max1 = max(max1, array[i] + i)
        min1 = min(min1, array[i] + i)
        max2 = max(max2, array[i] - i)
        min2 = min(min2, array[i] - i)

        # Calculating maximum absolute difference.
    return max(max1 - min1, max2 - min2)

#print(maxArr_brute(A))

print(maxArr_fast(A))
