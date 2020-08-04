# Q3 Valid Pallindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sh = s.lower()
        new = ""
        for i in sh:
            if ((i >= 'a' and i <= 'z') or (i >= '0' and i <= '9')):
                new += i
        if new == new[::-1]:
            return True
        else:
            return False
        
        
