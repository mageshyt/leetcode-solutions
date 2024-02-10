class Solution:
    # time complexity: O(n*sqrt(n)), space complexity: O(n)
    def numSquares(self, n: int) -> int:

        dp = {}
        squares = []
        for i in range(1, n):
            sq = pow(i, 2)
            if sq > n:
                break
            squares.append(sq)

        def dfs(n):
            if n == 0:
                return 0
            if n in dp:
                return dp[n]
            res = float('inf')
            for sq in squares:
                if n - sq >= 0:
                    res = min(res, dfs(n - sq) + 1)
            dp[n] = res
            return res

        return dfs(n)

    # bottom up approach

    def numSquares(self, n: int) -> int:
        if n <=1:
            return n
        dp = [float('inf')] * (n + 1)
        squares = []
        for i in range(1, n):
            sq = pow(i, 2)
            if sq > n:
                break
            squares.append(sq)
        # to make  0 we need 0 perfect squares
        dp[0] = 0

        for i in range(1, n + 1):
            for sq in squares:
                if i - sq >= 0:
                    dp[i] = min(dp[i], dp[i - sq] + 1)

        return dp[n]


print("Number of perfect squares for 12 is ", Solution().numSquares(12))
