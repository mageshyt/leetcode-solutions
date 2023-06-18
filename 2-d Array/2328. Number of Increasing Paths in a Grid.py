class Solution:

    def __init__(self) -> None:
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0]*cols for _ in range(rows)]
        res = 0
        mod = 10**9+7

        for row in range(rows):
            for col in range(cols):
                res = (res + self.dfs(grid, dp, row, col)) % mod

        return res % mod

    def dfs(self, grid, dp, row, col):

        # base case
        if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0])):
            return 0
        mod = 10**9+7

        if (dp[row][col] != 0):
            return dp[row][col]

        res = 1  # we will always have one path

        for direction in self.directions:
            newRow = row+direction[0]
            newCol = col+direction[1]

            if self.isValid(grid, newRow, newCol) and grid[newRow][newCol] > grid[row][col]:
                res = (res % mod + self.dfs(grid, dp, newRow, newCol) %
                       mod) % mod

        dp[row][col] = res

        return res

    def isValid(self, grid, row, col):
        if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0])):
            return False

        return True
