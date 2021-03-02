from functools import cmp_to_key

A = [10, 23, 5, 23, 57, 21]
#A =[3, 30, 34, 5, 9]

def double_it(num):
    return num + num


#Example 1
#A = list(map(double_it, A))  # call a function which doubles the numbers

#Example 2
#num1 = [1,6,3]
#num2 = [2,4,5]
#A = list(map(lambda a,b: 1 if a > b else 0, num1, num2)) # basically a lambda function which acts on two number arrays
#A = list(map(lambda a,b: 1 if a > b else 0, num1, num2))

#Example 3 - arrange the array so that you get the largest number:
A = map(str,A)
key_func = cmp_to_key(lambda a , b: 1 if a + b > b + a else -1)
print(''.join(sorted(A, key=key_func,reverse=True)))




