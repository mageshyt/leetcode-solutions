"""There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.



Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Example 2:

Input: n = 1
Output: 0


Constraints:

1 <= n <= 1000"""

class Solution:
    def minSteps(self, n: int) -> int:
        # base case
        if n == 1:
            return 0

        cache={}

        def dp(count, copied):
            if count == n:
                return 0
            if count > n:
                return float('inf')

            if (count, copied) in cache:
                return cache[(count, copied)]



            # copy & paste
            copy= 1 + dp(count+copied, copied)

            paste= 2 + dp(count + count, count)

            cache[(count, copied)] = min(copy, paste)
            return cache[(count, copied)]

        return dp(1, 1) +1

print(Solution().minSteps(9)) # 6
print(Solution().minSteps(3)) # 3
print(Solution().minSteps(1)) # 0