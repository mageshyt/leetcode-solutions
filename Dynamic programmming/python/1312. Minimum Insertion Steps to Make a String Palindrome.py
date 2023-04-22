"""Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel"."""


class Solution:
    def minInsertions(self, string: str) -> int:
        def dp(i, j):
            if i >= j:
                return 0
            if string[i] == string[j]:
                return dp(i+1, j-1)
            else:
                return 1+min(dp(i+1, j), dp(i, j-1))
            
            

        return dp(0, len(string)-1)

    def minInsertions2(self, string: str) -> int:
        n = len(string)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                print('1 ', string[i], ' 2', string[j])
                if string[i] == string[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i+1][j], dp[i][j-1])
        print(dp)
        return dp[0][n-1]


if __name__ == "__main__":
    string = "tldjbqjdogipebqsohdypcxjqkrqltpgviqtqz"

    print(Solution().minInsertions(string))


def minInsertions2(self, string: str) -> int:
    n = len(string)
    dp = [[0]*n for _ in range(n)]
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if string[i] == string[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1+min(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]
