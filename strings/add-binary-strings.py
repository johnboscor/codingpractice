#https://www.interviewbit.com/problems/add-binary-strings/

a = "1010110111001101101000"
b = "1000011011000000111100110"

'''
# Using- convert to binary and convert back method
def get_decimal(num):
    i = 0
    val = 0
    while num > 0:
        val += num%10 * (2**i)
        num = num // 10
        i += 1
    return val

print(str('{:b}'.format( (get_decimal(int(a)) + get_decimal(int(b)))))) 
'''
'''
a = [i for i in a]
b = [i for i in b]

if len(a) > len(b):
    b = [ '0' for i in range(len(a) - len(b))] + b
elif len(b) > len(a):
    a = ['0' for i in range(len(b) - len(a))] + a
'''
max_len=max(len(a),len(b))
a = a.zfill(max_len)
b = b.zfill(max_len)

print(a)
print(b)
sum = 0
carry = 0
c = ""
lg = len(a) - 1
while lg >= 0:
    sum_val = int(a[lg]) + int(b[lg]) + carry
    c = str(sum_val % 2) + c
    carry = 0
    if sum_val >= 2:
        carry = 1
    lg -= 1
    if lg < 0 and carry:
        c = '1' + c
print(f"Sum is {c}")
