from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        w_s, w_e = 0, 1
        sub_count = 0
        pre_sum = nums[0]
        while w_s < len(nums):
            pass
        return sub_count


print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2))
