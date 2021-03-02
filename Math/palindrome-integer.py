
num = 102
a = ''.join([ i for i in str(num)])
a = a[len(a)::-1]
if int(a) == num:
    print("Palindrome")
else:
    print("Not palindrome")
