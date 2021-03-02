arr = [23,45,56,76,67,19,0,56, 23]


def merge_sort(a):
    if len(a) > 1:
        mid = len(a)//2   # use // or else it will return floating point
        left = a[:mid]
        right = a[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1





print(f"Before sorting: {arr}")
merge_sort(arr);
print(f"After sorting: {arr}")