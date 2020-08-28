'''A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.
We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
The rules of Goat Latin are as follows:
If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin. '''

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
                
                
        
