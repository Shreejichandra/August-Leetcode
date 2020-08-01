# Q1 Detect Capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if (word.isupper() or word.islower()):
            ans = "True"
        elif (word == word.capitalize()):
            ans = True
        else:
            ans = False
        return ans
