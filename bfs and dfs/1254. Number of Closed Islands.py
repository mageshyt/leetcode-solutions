"""Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1"""


class Solution:
    def closedIsland(self, grid) -> int:
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, grid):
            rows = len(grid)
            cols = len(grid[0])

            # out of bounds

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if grid[r][c] == 1:
                return

            # mark as visited
            grid[r][c] = 1

            # go through all the neighbors

            for dx, dy in dir:
                dfs(r+dx, c+dy, grid)

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        # first make border 1s

        for i in range(rows):
            for j in range(cols):

                if(i*j == 0 and grid[i][j] == 0):  # first row and first column
                    dfs(i, j, grid)

                # last row and last column
                if(i == rows-1 or j == cols-1 and grid[i][j] == 0):
                    dfs(i, j, grid)

        # now count the number of islands

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    count += 1
                    dfs(i, j, grid)
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.closedIsland([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [
          1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]))
    print(s.closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))
