class Solution:
    def minimumTotal(self, triangle) -> int:

        dp = [0]*(len(triangle)+1)

        for row in triangle[::-1]:
            for i in range(len(row)):
                dp[i] = row[i] + min(dp[i], dp[i+1])

             
        return dp[0]


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

obj = Solution()

obj.minimumTotal(triangle)
