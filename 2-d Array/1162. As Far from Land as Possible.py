'''Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.'''

import collections


class Solution:
    def maxDistance(self, grid) -> int:
        # 1 - land
        # 0 - water

        rows = len(grid)
        cols = len(grid[0])

        queue = collections.deque()  # queue for BFS traversal

        for i in range(rows):
            for j in range(cols):
                # if land, add to queue
                if grid[i][j]:
                    queue.append((i, j))

        # multiple source BFS
        res = -1  # if no land or water exists in the grid, return -1.

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            x, y = queue.popleft()

            res = grid[x][y]  # distance from land

            # check all 4 directions

            for dx, dy in directions:
                new_row = x + dx  # new row
                new_col = y + dy  # new col

                # if neighbor is out of bounds and grid is water
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 0:

                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = grid[x][y] + 1  # update distance

        return res-1 if res > 1 else -1


if __name__ == '__main__':
    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    print(Solution().maxDistance(grid))
