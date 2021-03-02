#https://www.interviewbit.com/problems/sorted-insert-position/

A = [1]
B = 0
def searchInsert(A, B):
    maxi = len(A)
    mini = 0
    while mini < maxi:
        mid = mini + ((maxi - mini) // 2)
        if A[mid] == B:
            return mid
        if A[mid] > B:
            maxi = mid
        else:
            mini = mid + 1

    return maxi

print(searchInsert(A,B))