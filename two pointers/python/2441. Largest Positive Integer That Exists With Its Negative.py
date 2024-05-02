"""
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.



Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.
Example 2:

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
Example 3:

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.
"""

from collections import defaultdict
from typing import List
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # create a dictionary to store the index of each number
        num_idx=defaultdict(list)
        for i,num in enumerate(nums):
            num_idx[num].append(i)

        res=-1
        for num in nums:
            if -num in num_idx:
                res=max(res,num)

        return res


# Time complexity: O(N)
# Space complexity: O(N)
#
nums = [-1,2,-3,3]
nums = [-1,10,6,7,-7,1]
nums = [-10,8,6,7,-2,-3]

print(Solution().findMaxK(nums))
