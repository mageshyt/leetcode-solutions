
from typing import List
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern = {} # pattern -> count

        for currRow in matrix:
            row_pttern="".join(
                "T" if num == currRow[0] else "F" for num in currRow
            )

            pattern[row_pttern] = pattern.get(row_pttern,0)+1
        return max(pattern.values(), default=0)


        
