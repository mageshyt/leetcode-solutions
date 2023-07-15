"""Given two strings s and t, return the number of distinct 
subsequences
 of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}  # Memoization dictionary to store already computed results

        def dfs(i: int, j: int) -> int:
            # Base cases
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            if s[i] == t[j]:
                # If the characters match, we can either include or skip the character in s
                dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # If the characters don't match, we can only skip the character in s
                dp[(i, j)] = dfs(i + 1, j)

            return dp[(i, j)]

        return dfs(0, 0)
