"""There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
"""

class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        def helper(i: int, j: int) -> int:
            print  (i,j)
            if i > j:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            # Skip identical characters
            while i < j and s[i] == s[i + 1]:
                i += 1

            res = helper(i + 1, j) + 1

            # Try covering the current character with other characters
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    res = min(res, helper(i, k - 1) + helper(k + 1, j))
            memo[(i, j)] = res
            return memo[(i, j)]

        helper(0, len(s) - 1)
        print(memo)


if __name__ == "__main__":
    s=Solution()
    print(s.strangePrinter("tbgtgb"))




