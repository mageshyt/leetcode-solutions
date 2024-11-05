"""
You are given an integer array nums. A subsequence of nums is called a square streak if:

The length of the subsequence is at least 2, and
after sorting the subsequence, each element (except the first element) is the square of the previous number.
Return the length of the longest square streak in nums, or return -1 if there is no square streak.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
"""
from typing import List
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        n=len(nums)
        # convert to set for O(1) lookup
        unqiue=set(nums)
        longest_streak=0

        for start in nums:
            curr_streak=0
            curr=start

            while curr in unqiue:
                curr_streak+=1
                curr*=curr



        return longest_streak if longest_streak>1 else -1

# Time: O(n^2)
# Space: O(n)
print(Solution().longestSquareStreak([1,4,16,64])) # 4
print(Solution().longestSquareStreak([3,4,16,8,2])) # 4


