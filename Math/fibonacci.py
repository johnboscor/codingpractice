n = 5

#normal fibonacci with recurision.. very slow for large numbers
'''
def fib(n):
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)
'''
'''
#fibonacci with memoization and recursion.
fn = [-1] * 41
fn[0] = 0
fn[1] = 1
def fib(n):
    if fn[n] != -1:
        return fn[n]

    fn[n] = fib(n - 1) + fib(n - 2)
    return fn[n]
'''
#0 1 1 2 3 5
#fib iterative
def fib(n):
    if n <= 1:
        return n
    sum = 2
    prev = 1
    for i in range(2,n):
        temp = sum
        sum += prev
        prev = temp
    return(sum)


print(fib(40))
#0 1 1 2 3 5 8 13 21

