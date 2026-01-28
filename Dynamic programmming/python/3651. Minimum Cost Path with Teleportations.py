"""
You are given a m x n 2D integer array grid and an integer k. You start at the top-left cell (0, 0) and your goal is to reach the bottom‐right cell (m - 1, n - 1).

There are two types of moves available:

Normal move: You can move right or down from your current cell (i, j), i.e. you can move to (i, j + 1) (right) or (i + 1, j) (down). The cost is the value of the destination cell.

Teleportation: You can teleport from any cell (i, j), to any cell (x, y) such that grid[x][y] <= grid[i][j]; the cost of this move is 0. You may teleport at most k times.

Return the minimum total cost to reach cell (m - 1, n - 1) from (0, 0).


"""
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:

        n, m = len(grid), len(grid[0])

        cost = [[float('inf')]*m for _ in range(n)]

        # its always take 0 cost to reach the end cell from itself
        cost[-1][-1] = 0

        tcost = [float('inf')] * (max(max(row) for row in grid) + 1)

        for t in range(k+1):
            for i in range(n-1,-1,-1):
                for j in range(m-1,-1,-1):
                    if i == n-1 and j == m-1:
                        continue



                    if i < n - 1:
                        cost[i][j]= min(cost[i][j], cost[i+1][j] + grid[i+1][j])

                    if j < m - 1:
                        cost[i][j] = min(cost[i][j], cost[i][j+1] + grid[i][j+1])

                    if t > 0:
                        cost[i][j] = min(cost[i][j], tcost[grid[i][j]])

            # compute tcost for next t
            for i in range(n-1,-1,-1):
                for j in range(m-1,-1,-1):
                    tcost[grid[i][j]] = min(tcost[grid[i][j]], cost[i][j])


            for i in range(1, len(tcost)):
                tcost[i] = min(tcost[i], tcost[i-1])


        return cost[0][0]


if __name__ == "__main__":
    s = Solution()
    print(s.minCost([[1,2],[2,3],[3,4]], 1))  # Output: 7
