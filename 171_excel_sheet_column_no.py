#Given a column title as appear in an Excel sheet, return its corresponding column number.


class Solution:
    def titleToNumber(self, s: str) -> int:
        sum_ = 0
        for i in range(len(s)):
            sum_ *= 26
            sum_ += ord(s[i]) - 64
        return sum_
        
