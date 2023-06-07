class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[-1]*cols for _ in range(rows)]

        def dfs(row, col):
            # for out of bounds and obstacles

            if row >= rows or col >= cols or obstacleGrid[row][col] == 1:
                return 0
            
            # already calculated

            if dp[row][col] != -1:
                return dp[row][col]
            

            # last cell
            if row == rows-1 and col == cols-1:
                return 1
            
            # right and down
            right = dfs(row, col+1)
            down = dfs(row+1, col)

            dp[row][col] = right+down


            return dp[row][col]
        
        return dfs(0, 0)
    

# Time complexity: O(m*n)
# Space complexity: O(m*n)
