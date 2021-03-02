
from math import *

#input_arry=[42,53,8,5,21,56,2]
input_arry = []
print("Enter 5 numbers to be sorted: ")
for k in range(5):
    val = int(input())
    input_arry.append(val)

print(f"Input array is: {input_arry}")
length=len(input_arry)
for i in range(length):
    for j in range(i,length):
        if input_arry[i] > input_arry[j]:
            temp=input_arry[i]
            input_arry[i] = input_arry[j]
            input_arry[j] = temp

print(f"Array after bubble sort is : {input_arry}")

