"""
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of elements in both sections is equal, or can be made equal by discounting at most one single cell in total (from either section).
If a cell is discounted, the rest of the section must remain connected.
Return true if such a partition exists; otherwise, return false.

Note: A section is connected if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.

 

Example 1:

Input: grid = [[1,4],[2,3]]

Output: true

Explanation:



A horizontal cut after the first row gives sums 1 + 4 = 5 and 2 + 3 = 5, which are equal. Thus, the answer is true.
Example 2:

Input: grid = [[1,2],[3,4]]

Output: true

Explanation:



A vertical cut after the first column gives sums 1 + 3 = 4 and 2 + 4 = 6.
By discounting 2 from the right section (6 - 2 = 4), both sections have equal sums and remain connected. Thus, the answer is true.
Example 3:

Input: grid = [[1,2,4],[2,3,5]]

Output: false

Explanation:



A horizontal cut after the first row gives 1 + 2 + 4 = 7 and 2 + 3 + 5 = 10.
By discounting 3 from the bottom section (10 - 3 = 7), both sections have equal sums, but they do not remain connected as it splits the bottom section into two parts ([2] and [5]). Thus, the answer is false.
Example 4:

Input: grid = [[4,1,8],[3,2,6]]

Output: false

Explanation:

No valid cut exists, so the answer is false.

 

Constraints:

1 <= m == grid.length <= 105
1 <= n == grid[i].length <= 105
2 <= m * n <= 105
1 <= grid[i][j] <= 105
"""
from typing import List
from collections import defaultdict
class Solution:
    def canPartitionGrid(self,grid:List[List[int]]):
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)

        bottom_feq = defaultdict(int)
        top_feq = defaultdict(int)
        
        for row in grid:
            for val in row:
                bottom_feq[val] += 1

        top_sum = 0
        for i in range(m - 1):
            for j in range(n):
                val = grid[i][j]
                top_sum += val
                top_feq[val] += 1
                bottom_feq[val] -= 1
            bottom_sum = total_sum - top_sum

            if top_sum == bottom_sum:
                return True
            
            diff = abs(top_sum - bottom_sum)

            if top_sum > bottom_sum:
                freq,r1,r2 = top_feq,0,i
            else:
                freq,r1,r2 = bottom_feq,i + 1,m - 1


            rows = r2 - r1 + 1

            if rows*n ==1 :
                continue
            elif rows == 1:
                if grid[r1][0] == diff or grid[r1][n - 1] == diff:
                    return True
                
            elif freq.get(diff,0) > 0:
                return True
            
        return False
   