
from typing import List
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        result = []

        direction_index = 0
        r, c = rStart, cStart

        step = 1

        while len(result) < rows * cols:
            for _ in range(2):
                dr, dc = directions[direction_index]

                for _ in range(step):

                    # in bounce and add to result
                    if(0<=r<rows and 0<=c<cols):
                        result.append([r,c])

                    r,c= r+dr,c+dc

                direction_index=(direction_index+1)%4
            # increase step after 2 directions
            step+=1



        return result


# Time: O(max(rows, cols)^2)
# Space: O(rows * cols)

print(Solution().spiralMatrixIII(1, 4, 0, 0)) # [[0,0],[0,1],[0,2],[0,3]]

