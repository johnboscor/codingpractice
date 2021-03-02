arr = "Mr John Smith"
arr= arr.split()
print(arr)
arr1 = []
for i in arr:
    arr1 += i + '%20'
arr1 = ''.join(arr1).rstrip('%20')

print(arr1)