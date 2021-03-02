

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [4,3,5,6,2,1,8,7]
print("Before sort:",arr)
insertionSort(arr)
print("After sort:",arr)