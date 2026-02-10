"""
You are given an integer array nums.

A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

Return the length of the longest balanced subarray.

 

Example 1:

Input: nums = [2,5,4,3]

Output: 4

Explanation:

The longest balanced subarray is [2, 5, 4, 3].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.
Example 2:

Input: nums = [3,2,2,5,4]

Output: 5

Explanation:

The longest balanced subarray is [3, 2, 2, 5, 4].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.
"""

from collections import defaultdict
from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        maxLength = 0

        for i in range(len(nums)):
            evenSet = set()
            oddSet = set()

            for j in range(1, len(nums)-i+1):
                if nums[i+j-1] % 2 == 0:
                    evenSet.add(nums[i+j-1])
                else:
                    oddSet.add(nums[i+j-1])

                if len(evenSet) == len(oddSet):
                    maxLength = max(maxLength, j)
        return maxLength

