from math import *
i=0
j=0
for i in range(0,5):
    for j in range(0,i):
        print("*", end=' ')
    print('\n')
i=0
while i<10:
    print(i)
    i += 1

while True:
    val=input("Enter a number: ")
    if int(val) == 1:
        print(f"Entered number is: {val}")
    elif int(val) == 2:
        print("Entered number is: " + str(val))
    else:
        print("Number isn't valid")
        break;

