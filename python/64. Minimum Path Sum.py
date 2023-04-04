class Solution:
    def minPathSum(self, grid) -> int:

        rows = len(grid)
        cols = len(grid[0])
        max_val = max(rows, cols)
        res = [[max_val+1]*(cols+1) for i in range(rows+1)]

        res[rows-1][cols] = 0  # last cell must be 0

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                min_step = min(res[row+1][col], res[row]
                               [col+1])  # right and down

                res[row][col] = grid[row][col] + \
                    min_step  # add current cell value

        return res[0][0]


if __name__ == '__main__':
    grid = [[1, 2, 3], [4, 5, 6]]
    print(Solution().minPathSum(grid))
