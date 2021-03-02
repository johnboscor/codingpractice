#https://www.interviewbit.com/problems/rearrange-array/
#https://www.quora.com/How-can-I-rearrange-a-given-array-so-that-Arr-I-becomes-Arr-Arr-I-with-O-1-extra-space
# use the formula to encode: val = (a[a[i]]%n)*n + a[i]
# to decode use val = a[i] % n


a = [3 , 0, 1 , 4, 2]
print(a)
lg = len(a)
#encoding
for i in range(lg):
    a[i] = (a[a[i]] % lg)*lg + a[i]
    print(a)
#decode
for i in range(lg):
    a[i] //= lg

print(a)
