#https://www.interviewbit.com/problems/search-for-a-range/

A = [1,2]
B = 2
def searchRange(A, B):
    maxi = len(A)
    mini = 0

    C = []
    while mini < maxi:
        mid = mini + ((maxi - mini) // 2)
        if A[mid] == B:
            low = mid
            high = mid
            C = [0,0]
            while low >= 0 and A[low] == B:
                C[0] = low
                low -= 1
            while high < maxi and A[high] == B:
                C[1] = high
                high += 1
            break

        if A[mid] > B:
            maxi = mid
        else:
            mini = mid + 1
    else:
        C = [-1,-1]
    return C

print(searchRange(A,B))