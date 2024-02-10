from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}

        def dfs(i):
            # base case
            if i <= 0:
                return 0
            if i in cache:
                return cache[i]

            ans, max_val = 0, 0

            # loop through max k elements
            for n in range(i,min(k+1, i+1)):
                max_val = max(max_val, arr[i-n])
                ans = max(ans, dfs(i-n)+max_val*n)
            cache[i] = ans
            return ans

        return dfs(len(arr))


print(Solution().maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))
