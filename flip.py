#You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN.
#In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR.
#By flipping, we mean change character 0 to 1 and vice-versa.

#see https://www.interviewbit.com/problems/flip/

#A = [0 , 1 , 0]
A = [1,1,0,1,0,1,0,0,0,1]


B = [1 if i == 0 else -1 for i in A]
print(B)

max_sum = float('-inf')
start = 0
curr_sum=0
res = []
for i in range(len(B)):
    curr_sum += B[i]
    if curr_sum < 0:
        start = i + 1
        curr_sum = 0
        continue
        
    if curr_sum > max_sum and curr_sum >= 0:
        max_sum = curr_sum
        res = [start+1, i+1]


print(res)
