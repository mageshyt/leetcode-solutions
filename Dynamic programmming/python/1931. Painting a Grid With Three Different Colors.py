"""
You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 1, n = 1
Output: 3
Explanation: The three possible colorings are shown in the image above.
Example 2:


Input: m = 1, n = 2
Output: 6
Explanation: The six possible colorings are shown in the image above.
Example 3:

Input: m = 5, n = 5
Output: 580986
 

Constraints:

1 <= m <= 5
1 <= n <= 1000

"""
from collections import defaultdict
from itertools import product

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        # Generate valid colorings for one column
        def generate_valid_columns():
            valid = []
            for colors in product(range(3), repeat=m):
                if all(colors[i] != colors[i+1] for i in range(m-1)):
                    valid.append(colors)
            return valid

        valid_columns = generate_valid_columns()

        # Check if two columns are compatible
        def is_compatible(col1, col2):
            return all(c1 != c2 for c1, c2 in zip(col1, col2))

        # DP table
        dp = defaultdict(int)
        for col in valid_columns:
            dp[col] = 1  # Initialize first column

        for _ in range(n - 1):
            new_dp = defaultdict(int)
            for prev_col in dp:
                for curr_col in valid_columns:
                    if is_compatible(prev_col, curr_col):
                        new_dp[curr_col] = (new_dp[curr_col] + dp[prev_col]) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD

