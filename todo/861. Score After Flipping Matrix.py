
from typing import List
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])

        for row in range(rows):
            # if the first element of the row is 0, then flip the row
            if grid[row][0]==0:
                for col in range(cols):
                    grid[row][col]^=1

        for col in range(cols):
            count=0 # count of 1s in the column
            for row in range(rows):
                count+=grid[row][col]
            # if the number of 1s is less than the number of 0s, then flip the column
            if count<rows-count:
                for row in range(rows):
                    grid[row][col]^=1


        result=0
        for row in range(rows):
            result+=int("".join(map(str,grid[row])),2)

        return result

# Time complexity: O(rows*cols)
# Space complexity: O(1)
