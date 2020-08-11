# H-Index

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cit = sorted(citations)
        n = len(cit)
        h = 0
        for i in range(n):
            if cit[i] >= n - i:
                return n - i
        return h
