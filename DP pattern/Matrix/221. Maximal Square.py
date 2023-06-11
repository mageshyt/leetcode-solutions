"""Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4"""


class Solution:
    def maximalSquare(self, matrix) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        cache = {}  # cache for memoization (key: (row, col), value: min step

        def helper(row, col):
            # out of bound

            if row >= rows or col >= cols:
                return 0

            # if already calculated
            if (row, col) in cache:
                return cache[(row, col)]

            down = helper(row+1, col)

            right = helper(row, col+1)

            diag = helper(row+1, col+1)

            # if current cell is 1
            if matrix[row][col] == '1':

                # min of all three +1
                cache[(row, col)] = min(down, right, diag)+1

                return cache[(row, col)]

            # if current cell is 0
            else:
                cache[(row, col)] = 0
                return 0

        # iterate over all cells
        helper(0, 0)
        return max(cache.values())**2


if __name__ == "__main__":
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]

    print(Solution().maximalSquare(matrix))
