"""You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

import collections


class Solution:
    def orangesRotting(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 1. build the initial set of rotten oranges
        # we use a deque instead of a list to make popleft() more efficient

        rotten = collections.deque()

        fresh_oranges = 0  # count fresh oranges

        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))  # add the rotten orange to the queue
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        while rotten and fresh_oranges > 0:

            for _ in range(len(rotten)):
                r, c = rotten.popleft()

                # 2. check all 4 directions
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # base case 1: out of bounds

                    if(min(nr, nc) < 0 or nr >= rows or nc >= cols):
                        continue

                    if grid[nr][nc] != 1:
                        continue

                    # 3. mark the orange as rotten
                    grid[nr][nc] = 2

                    # 4. add the newly rotten orange to the queue
                    rotten.append((nr, nc))

                    # 5. decrement the count of fresh oranges by 1
                    fresh_oranges -= 1
            time += 1
        # return elapsed minutes if no fresh oranges left
        return -1 if fresh_oranges else time
