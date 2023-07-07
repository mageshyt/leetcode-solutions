from typing import List

"""Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_len = float('inf')

        window_sum = 0

        ws = 0  # window start

        for window_end in range(len(nums)):
            # add the value to the sum

            window_sum += nums[window_end]

            while window_sum >= target:

                min_len = min(min_len, (window_end-ws)+1)
                window_sum -= nums[ws]
                ws += 1

        return min_len if min_len != float('inf') else 0


nums = [2, 3, 1, 2, 4, 3]

print(Solution().minSubArrayLen(7, nums))
