arr = [1, 2, 3]
dep = [2, 3, 4]
#arr = [ 17, 0, 45, 11, 16, 43, 15, 42, 2, 41, 0, 27, 37, 25, 17, 42, 24, 23, 11, 4, 29, 39, 6, 10, 42, 16, 17, 39, 1 ]
#dep = [ 25, 24, 52, 51, 26, 46, 25, 45, 9, 51, 49, 48, 51, 66, 65, 57, 69, 43, 50, 9, 32, 55, 10, 58, 62, 46, 19, 87, 12 ]
K = 2


def hotel(arr, dep, K):


    A = [0] * (max(dep) + 1)

    # print(A)

    for i in range(len(arr)):
        A[arr[i]] += 1
    for i in range(len(dep)):
        A[dep[i]] -= 1

    # print(A)

    max_val = 0
    curr_sum = 0
    for i in range(len(A)):
        curr_sum += A[i]
        max_val = max(curr_sum, max_val)
        if curr_sum < 0:
            curr_sum = 0

    return (False if max_val > K else True)


print(hotel(arr, dep, K))