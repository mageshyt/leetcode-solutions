"""Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        meme = {}

        def helper(x, n):

            # base case
            if n == 0:
                return 1
            if n == 1:
                return x

            if n in meme:
                return meme[n]

            if n == -1:
                return 1/x

            # logic
            meme[n] = helper(x, n//2) * helper(x, n//2) * helper(x, n % 2)
            return meme[n]
        return helper(x, n)


# Time Complexity: O(logn)
# Space Complexity: O(logn)

print(Solution().myPow(2.00000, 10))
