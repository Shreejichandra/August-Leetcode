''' Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.'''

from collections import defaultdict

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        val = 1
        ans = []
        for i in nums:
            d[i] += 1
        for key, value in d.items(): 
            if val != value: 
                ans.append(key)
                
        return (set(ans))
        
