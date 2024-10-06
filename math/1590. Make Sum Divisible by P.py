from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        n = len(nums)
        target = sum(nums) % p
        if target == 0:
            return 0

        prefixSum = 0
        prefixSumToIndex = {0: -1}
        minSubarrayLength = n
        currentSum = 0

        for i, num in enumerate(nums):
            prefixSum += num
            prefixSum %= p # to avoid overflow
            prefixSumToIndex[prefixSum] = i
        

            currentSum += num
            currentSum %= p

            key= (currentSum - target) % p

            if key in prefixSumToIndex:
                size= i - prefixSumToIndex[key]
                minSubarrayLength = min(minSubarrayLength, size)


        return minSubarrayLength if minSubarrayLength < n else -1

s=Solution()

print(s.minSubarray([3,1,4,2], 6)) # 1

