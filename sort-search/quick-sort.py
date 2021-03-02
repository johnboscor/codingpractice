def findPivot(arr,start,end):
    i = start - 1
    pivot = arr[end]
    for j in range(start,end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return i+1


def quickSort(arr, start,end):

    if start < end:
        pivot = findPivot(arr,start,end)
        quickSort(arr,start,pivot-1)
        quickSort(arr,pivot+1,end)

arr = [4,5,3,2,1,8,6]
print("Before sort: ",arr)
quickSort(arr,0,len(arr)-1)
print("After sorting: ",arr)
