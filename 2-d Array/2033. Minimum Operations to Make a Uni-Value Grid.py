from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # sort the grid
        n=len(grid)
        values=sorted([val for row in grid for val in row])

        diff=[abs(val-values[0]) % x for val in values]

        if any(d !=0 for d in diff):
            return -1

        # get the median
        median=values[len(values)//2]
        operations=sum(abs(val-median)//x for val in values)
        return operations


sol=Solution()
print(sol.minOperations([[2,4],[6,8]],2)) #4

