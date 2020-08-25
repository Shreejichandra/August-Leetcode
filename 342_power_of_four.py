# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        n = 1
        if num == 1:
            return True
        
        while (n < num):
            n = n * 4
            if n == num:
                return True
            
        return False
