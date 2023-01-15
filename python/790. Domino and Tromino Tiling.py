'''You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are show above.
Example 2:

Input: n = 1
Output: 1'''


class Solution:
    def numTilings(self, n: int) -> int:

        if(n == 1):
            return 1
        if(n == 2):
            return 2
        if(n == 3):
            return 5
        dp = [0]*(n+1)

        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

    # analysis:
        # pattern 2 x (prev result) +1  for 2x1 = 1 , 2x2 = 2, 2x3 = 5 , 2x4= (2 x 5) + 1 = 11, 2x5 = 2 x 11 + 1 = 23
        for i in range(4, n+1):
            dp[i] = (2*dp[i-1]+dp[i-3]) % (10**9+7)
        return dp[n]
