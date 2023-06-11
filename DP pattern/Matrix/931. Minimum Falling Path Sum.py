"""Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

"""


class Solution:
    def minFallingPathSum(self, matrix) -> int:
        # logic lets go from bottom to top

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0] = matrix[0]

        for row in range(1, rows):
            for col in range(cols):
                # if first col [ i can only come from top or top right]
                if col == 0:
                    min_val = min(dp[row - 1][col], dp[row - 1][col + 1])

                    dp[row][col] = matrix[row][col] + min_val

                # if last col [ i can only come from top or top left]
                elif col == cols - 1:
                    min_val = min(dp[row - 1][col], dp[row - 1][col - 1])

                    dp[row][col] = matrix[row][col] + min_val

                else:
                    # [ i can come from top or top left or top right]
                    min_val = min(dp[row - 1][col], dp[row - 1]
                                  [col - 1], dp[row - 1][col + 1])

                    # [row-1][col] -> top
                    # [row-1][col-1] -> top left
                    # [row-1][col+1] -> top right

                    dp[row][col] = matrix[row][col] + min_val

        return min(dp[-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
