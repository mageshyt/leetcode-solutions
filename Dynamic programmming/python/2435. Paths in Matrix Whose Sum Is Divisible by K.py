"""
You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.

Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:


Input: grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
Output: 2
Explanation: There are two paths where the sum of the elements on the path is divisible by k.
The first path highlighted in red has a sum of 5 + 2 + 4 + 5 + 2 = 18 which is divisible by 3.
The second path highlighted in blue has a sum of 5 + 3 + 0 + 5 + 2 = 15 which is divisible by 3.
Example 2:


Input: grid = [[0,0]], k = 5
Output: 1
Explanation: The path highlighted in red has a sum of 0 + 0 = 0 which is divisible by 5.
Example 3:


Input: grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
Output: 10
Explanation: Every integer is divisible by 1 so the sum of the elements on every possible path is divisible by k.
"""

from typing import  List
from collections import defaultdict
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        dp = defaultdict(int)
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        def dfs(row,col,rem_sum):

            if row < 0 or col < 0 or row >= m or col >= n:
                return 0
            if (row,col) == (m-1,n-1):
                total = (rem_sum + grid[row][col] ) % k
                return 1 if total == 0 else 0

            if (row,col,rem_sum) in dp:
                return dp[(row,col,rem_sum)]



            dp[(row,col,rem_sum)] = (
                dfs(row+1,col,(rem_sum + grid[row][col]) % k) % MOD +
                dfs(row,col+1,(rem_sum + grid[row][col]) % k) % MOD
            )
            return dp[(row,col,rem_sum)]

        return dfs(0,0,0) % MOD

print(Solution().numberOfPaths([[5,2,4],[3,0,5],[0,7,2]], 3)) # 2
print(Solution().numberOfPaths([[0,0]], 5)) # 1




