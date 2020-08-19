#Goat Latin

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = S.split(" ")
        x = 1
        extra = "ma"
        new = ""
        for i in s:
            if i[0] in vowels:
                word = i + extra + "a"*x
                
            else:
                word = i[1:]
                word += i[0] + extra + "a"*x
                
            new += word + " "
            x += 1
        return new.strip(" ")
                
                
        
