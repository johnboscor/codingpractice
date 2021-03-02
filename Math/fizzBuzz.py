N=6
arr=[i for i in range(1,N+1)]
#arr=["Fizz" if i%3 == 0 else i for i in range(1,N+1)]
print(arr)
for i in range(N+1):
    if i == 0:
        continue
    if i % 3 == 0 and i % 5 == 0:
        arr[i-1] = "FizzBuzz"
    elif i % 3 == 0:
        arr[i-1] = "Fizz"
    elif i % 5 == 0:
        arr[i-1] = "Buzz"
    else:
        continue


print(arr)