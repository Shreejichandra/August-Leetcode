'''Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.'''

from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = sorted(s, reverse = True)
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        count = 0
        flag = 0
        for key, value in d.items():
            if value % 2 == 0:
                count += value
            else:
                count += value - 1
                flag += 1
        if flag:
            return count + 1
        return count
            
            
            
        
