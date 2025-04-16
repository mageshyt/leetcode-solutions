"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.
"""

from collections import defaultdict
from typing import List
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        freq = defaultdict(int)
        left = 0
        pairs = 0

        for right in range(n):
            freq[nums[right]] += 1
            pairs += freq[nums[right]] - 1

            while pairs >= k:
                pairs -= freq[nums[left]] - 1
                freq[nums[left]] -= 1
                left += 1
                
            count += left


        return count
s=Solution()
nums = [1,1,1,1,1]
k = 10
print(s.countGood(nums, k)) # Output: 1
