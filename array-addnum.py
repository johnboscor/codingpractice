class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        length = len(A)

        carry = 0
        sum = 1
        c = []

        for i in range(length):
            val = A[length - 1 - i] + sum + carry
            sum = 0
            if val == 10:
                carry = 1
                c.append(0)
            else:
                carry = 0
                c.append(val)
        return(list(''.join(map(str, c))[::-1].lstrip('0')))


A = [ 0, 5, 6, 8, 6, 1, 2, 4, 9 ]
#A =  [ 1,9,9,9,9,9,9 ]
#A = [ 3, 0, 6, 4, 0 ]
#A =  [ 0, 0, 4, 4, 6, 0, 9, 6, 5, 1 ]
sol = Solution()
print(sol.plusOne(A))

