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
        
