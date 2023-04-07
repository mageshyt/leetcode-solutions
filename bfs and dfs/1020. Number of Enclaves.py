"""You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary."""


class Solution:
    def numEnclaves(self, grid) -> int:
        visited = set()
        # just run the dfs on the border alone

        rows = len(grid)
        cols = len(grid[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            if grid[r][c] == 0:  # if water we will
                return 0

            if (r, c) in visited:  # if visited we will return
                return 0

            visited.add((r, c))
            res = 1
            for dx, dy in directions:
                res += dfs(r+dx, c+dy)

            return res

        land, borderLand = 0, 0

        for i in range(rows):
            for j in range(cols):
                land += grid[i][j]  # if land we will add one else 0

                if (grid[i][j] and (i, j) not in visited and j in (0, cols-1) or i in (0, rows-1)):
                    borderLand += dfs(i, j)

        return land - borderLand


if __name__ == "__main__":
    s = Solution()
    print(s.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))

# Path: bfs and dfs/1021. Remove Outermost Parentheses.py


