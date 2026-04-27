"""
You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.

You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

 

Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).

"""

from typing import List
from collections import deque

class Solution:
    # dfs solution with backtracking
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: [(0, -1), (0, 1)], # left, right
            2: [(-1, 0), (1, 0)], # up, down
            3: [(0, -1), (1, 0)], # left, down
            4: [(0, 1), (1, 0)], # right, down
            5: [(0, -1), (-1, 0)], # left, up
            6: [(0, 1), (-1, 0)] # right, up
        }

        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r, c) == (m - 1, n - 1):
                return True

            visited.add((r, c))
            current_street = grid[r][c]

            for dr, dc in directions[current_street]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    next_street = grid[nr][nc]
                    if (-dr, -dc) in directions[next_street]: # check if the next street connects back to the current street
                        if dfs(nr, nc):
                            return True

            visited.remove((r, c))

        res = dfs(0, 0) 

        return res if res is not None else False

if __name__ == "__main__":
    solution = Solution()
    print(solution.hasValidPath([[2,4,3],[6,5,2]]))  # Output: true
    print(solution.hasValidPath([[1,2,1],[1,2,1]]))  # Output: false
    print(solution.hasValidPath([[1,1,2]]))          # Output: false

