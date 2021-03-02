#https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge_sort(self, A):
        if len(A) > 1:
            mid = len(A) // 2
            left = A[0:mid]
            right = A[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    A[k] = left[i]
                    i += 1
                else:
                    A[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                A[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                A[k] = right[j]
                j += 1
                k += 1
        return A

    def merge(self, A, B):
        A = A + B
        return self.merge_sort(A)

a = [-4, 3]
b = [-2,-2]
s = Solution()
print(s.merge(a,b))