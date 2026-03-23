"""
You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.

Notice that the modulo is performed after getting the maximum product.

 

Example 1:


Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
Output: -1
Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
Example 2:


Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).
Example 3:


Input: grid = [[1,3],[0,-4]]
Output: 0
Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).
"""
from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dp = {}
        rows,cols = len(grid), len(grid[0])

        def dfs(i , j):
            if (i ,j) in dp:
                return dp[i, j]

            if (i,j) == (rows - 1, cols - 1):
                return grid[i][j], grid[i][j]

            right = dfs(i, j + 1) if j + 1 < cols else None
            down = dfs(i + 1, j) if i + 1 < rows else None  

            if right and down:
                max_product = max(right[0] * grid[i][j], right[1] * grid[i][j], down[0] * grid[i][j], down[1] * grid[i][j])
                min_product = min(right[0] * grid[i][j], right[1] * grid[i][j], down[0] * grid[i][j], down[1] * grid[i][j])
            elif right:
                max_product = max(right[0] * grid[i][j], right[1] * grid[i][j])
                min_product = min(right[0] * grid[i][j], right[1] * grid[i][j])
            else:
                max_product = max(down[0] * grid[i][j], down[1] * grid[i][j])
                min_product = min(down[0] * grid[i][j], down[1] * grid[i][j])

            dp[i, j] = max_product, min_product
            return dp[i, j]

        max_product, _ = dfs(0, 0)
        return max_product % (10**9 + 7) if max_product >= 0 else -1






