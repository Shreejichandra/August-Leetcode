'''Given an array of integers A, We need to sort the array performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 0 <= k < A.length.
Reverse the sub-array A[0...k].
For example, if A = [3,2,1,4] and we performed a pancake flip choosing k = 2, we reverse the sub-array [3,2,1], so A = [1,2,3,4] after the pancake flip at k = 2.

Return an array of the k-values of the pancake flips that should be performed in order to sort A. Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.'''

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def flip(A, index):
            i, j = 0, index
            while i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            
        res = []
        n = len(A)
        largest = n
        for i in range(n):
            index = A.index(largest)
            flip(A, index)
            res.append(index + 1)
            flip(A, largest-1)
            res.append(largest)
            largest -= 1
        return res
    
            
        
        
