from collections import Counter


class Solution:
    def deleteAndEarn(self, nums) -> int:
        if not nums:
            return 0

        freq = [0] * (max(nums)+1)
        for n in nums:
            freq[n] += n

        dp = [0] * len(freq)
        dp[0] = freq[0]
        dp[1] = max(freq[0], freq[1])

        for i in range(2, len(freq)):
            dp[i] = max(dp[i-1], dp[i-2]+freq[i])

         

        return dp[-1]


nums = [3, 4, 2]
print(Solution().deleteAndEarn(nums))
