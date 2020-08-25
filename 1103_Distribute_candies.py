'''We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.'''


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
