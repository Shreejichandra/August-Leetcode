from collections import defaultdict
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.all_words = defaultdict(int)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        words = self.all_words
        words[word] = len(word)
     

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        words = self.all_words
        val = len(word)
        for key, value in words.items(): 
            count = 0
            if val == value:
                if key == word:
                    return True
                else:
                    for ch in range(val):
                        if (key[ch] == word[ch]) or word[ch] == '.':
                            count += 1
                            continue
                        else:
                            break
                    if count == len(word):
                        return True
                    
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
