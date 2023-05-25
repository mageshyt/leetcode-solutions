class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # base case
        if k == 0 or n >= k + maxPts:
            return 1.0

        # dp[i] = the probability of getting points i
        dp = {}
        window_sum = 0
        for i in range(k, k+maxPts):
            window_sum += 1 if i <= n else 0

        for i in range(k-1, -1, -1):
            dp[i] = window_sum/maxPts
            remove = 0  # the number of points that will be removed from the window

            if i+maxPts <= n:
                remove = dp.get(i+maxPts, 1)
                print(remove)

            window_sum += dp[i] - remove  # new window sum - old window sum

        return dp[0]


if __name__ == "__main__":
    n = 21
    k = 17
    maxPts = 10
    print(Solution().new21Game(n, k, maxPts))
