
#https://www.interviewbit.com/problems/triplets-with-sum-between-given-range/
#A = [0.6, 0.7, 0.8, 1.2, 0.4, 0 , 0, 0]
#B = [ "2.673662", "2.419159", "0.573816", "2.454376", "0.403605", "2.503658", "0.806191" ]
B = [ "0.366507", "0.234601", "2.126313", "1.372403", "2.022170", "0.308558", "2.120754", "1.561462" ]

#B = [ "0.480294", "0.298444", "1.109334" ]

A = []
for i in B:
    A.append(float(i))
print(A)

if len(A) < 3:
    print(False)
if len(A) == 3:
    print(True if sum(A) > 1 and sum(A) < 2 else False)
    exit(0)

A.sort()
print(A)

iter = len(A) - 2
for i in range(iter):
    sum_val = sum(A[i:i+3])
    if (sum_val > 1) and (sum_val < 2):
        print(True)
        break
