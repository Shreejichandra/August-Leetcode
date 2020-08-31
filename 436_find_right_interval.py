'''
'''
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        if not intervals: 
            return []
        if len(intervals) == 1: 
            return [-1]
        ref = dict()
        res = []

        for i in range(len(intervals)): 
            ref[intervals[i][0]] = i
            
        reflist = sorted(ref.items(), key=lambda x: x[0]) 
        
        for i in range(len(intervals)):
            left = 0
            right = len(reflist)-1
            mid = (left+right) // 2
            while left < mid and right > mid: 
                if intervals[i][1] == reflist[mid][0]: 
                    res.append(reflist[mid][1])
                    break
                elif intervals[i][1] > reflist[mid][0]:
                    left = mid
                    mid = (left+right)//2
                elif intervals[i][1] < reflist[mid][0]:
                    right = mid
                    mid = (left+right)//2
            if mid == left: 
                if intervals[i][1] <= reflist[mid+1][0]:
                    res.append(reflist[mid+1][1])
                else: 
                    res.append(-1)
        return (res)
