class Solution:
    def minPathSum(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # extra row and col for out of bound
        res = [[float('inf')]*(cols+1) for _ in range(rows+1)]

        # last cell is 0

        res[rows-1][cols] = 0

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                # min step for current cell

                right_step = res[row][col+1]
                down_step = res[row+1][col]

                min_step = min(right_step, down_step)

                res[row][col] = grid[row][col] + min_step

        return res[0][0]

        print(res)


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

print(Solution().minPathSum(grid))
