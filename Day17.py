#Distribute Candies to People


class Solution:
    def distributeCandies(self, c: int, n: int) -> List[int]:
        dis = 0
        left = c
        l = [0] * n
        i = 0
        while left:
            if i == n:
                i = 0
                dis += 1
                left -= dis
                if left >= 0:
                    l[i] += dis
                    i += 1
                else:
                    left += dis
                    l[i] += left
                    break
            else:
                dis += 1
                left -= dis
                if left >= 0:
                    l[i] += dis
                    i += 1
                else:
                    left += dis
                    l[i] += left
                    break


        return l
