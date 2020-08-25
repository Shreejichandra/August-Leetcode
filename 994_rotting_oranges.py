'''In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.'''

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
                    
        # edge case: no fresh orange
        if fresh == 0: 
            return 0
        
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if 0 <= x + dx < row and 0 <= y + dy < col and grid[x + dx][y + dy] == 1:
                        grid[x + dx][y + dy] = 2
                        q.append((x + dx, y + dy))
                        fresh -= 1
            ans += 1
        return ans -1 if fresh == 0 else -1
