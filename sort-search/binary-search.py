A = [1,2,3,4,5,6,7,8,9,10]

def binary_search_recur(n,low, high,A):
    if low > high:
        print("Not found")
        return False

    lg = len(A)

    mid = low + (high - low) // 2
    if A[mid] == n:
        print("found")
        return True
    elif A[mid] > n:
        binary_search_recur(n, low, mid-1,A)
    else:
        #print(A[mid +1:])
        binary_search_recur(n, mid+1,high,A)

def binary_search(n, A):
    lg = len(A)
    low = 0
    high = len(A) -1

    while low <= high:
        mid = low + (high - low) // 2
        if A[mid] == n:
            return True
        elif A[mid] < n:
            low = mid + 1
        else:
            high = mid -1
    return False


#print(binary_search(9,A))
print(binary_search_recur(10,0,len(A)-1,A))
