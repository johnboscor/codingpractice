
roman = {"I":1, "V": 5, "X": 10, "L":50, "C":100, "D": 500, "M":1000}

A = "MMMCMXCIX"
print(A[1:])
lg = len(A) -1
num = 0
num += roman[A[lg]]
lg -= 1
while lg >= 0:
    if roman[A[lg]] < roman[A[lg+1]]:
        num -= roman[A[lg]]
    else:
        num += roman[A[lg]]
    lg -= 1
print(num)


'''    
    if lg > 0:
        if ((A[lg] == "V" or A[lg] == "X") and A[lg-1] == "I") or \
            (A[lg] == "L" and A[lg - 1] == "X") or \
            (A[lg] == "C" and A[lg - 1] == "X") or \
            (A[lg] == "D" and A[lg - 1] == "C") or \
            (A[lg] == "M" and A[lg - 1] == "C"):
            num += roman[A[lg]] - roman[A[lg - 1]]
            lg -= 2
            continue
    num += roman[A[lg]]
    lg -= 1
'''