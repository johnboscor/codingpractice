def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(arr) - 1
    while arr[j] <= arr[i-1]:
        j -= 1

    arr[i-1], arr[j] = arr[j], arr[i-1]

    arr[i:] = arr[len(arr) -1: i-1: -1]

    return True



A = [0, 1, 2, 5, 3, 3, 0]
print(A)
print(next_permutation(A))
print(A)