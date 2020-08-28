'''Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.'''

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A) - 1
        k = 0
        while k < n:
            if A[k] % 2 == 0:
                k += 1
            else:
                while A[n] % 2 == 1 and n > k:
                    n -= 1
                A[k], A[n] = A[n], A[k]
                k += 1
                n -= 1
        return A
