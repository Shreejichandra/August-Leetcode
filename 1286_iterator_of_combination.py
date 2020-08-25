'''Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 '''
from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.all_combo = list(combinations(characters, combinationLength))

    def next(self) -> str:
        x = self.all_combo[0]
        self.all_combo.remove(x)
        return "".join(k for k in x)
    

    def hasNext(self) -> bool:
        return len(self.all_combo) != 0
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
