from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = {}

        def dfs(i, buy):
            # base case
            if i >= len(prices):
                return 0

            # memoization
            if (i, buy) in dp:
                return dp[(i, buy)]

            # recursive case
            if buy:
                dp[(i, buy)] = max(dfs(i+1, False) -
                                   prices[i] - fee, dfs(i+1, True))
            else:
                dp[(i, buy)] = max(dfs(i+1, True) + prices[i], dfs(i+1, False))

            return dp[(i, buy)]

        return dfs(0, True)


prices = [1, 3, 2, 8, 4, 9]

fee = 2

ob = Solution()

ans = ob.maxProfit(prices, fee)

print(ans)
