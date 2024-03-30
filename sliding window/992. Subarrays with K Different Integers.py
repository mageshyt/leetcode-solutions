"""Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
"""

from typing import List
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def helper(nums,k):
            freq=defaultdict(int)
            n=len(nums)
            left=0

            res=0

            for right in range(n):
                freq[nums[right]]+=1

                while len(freq) > k:
                    freq[nums[left]]-=1
                    if freq[nums[left]]==0:
                        del freq[nums[left]]
                    left+=1

                res+=right-left+1

            return res
        print(helper(nums,k),helper(nums,k-1))
        return helper(nums,k) -helper(nums,k-1)
    # three pointer
    def subarraysWithKDistinct2(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        res=0
        l_far,l_close=0,0

        for r in range(len(nums)):
            count[nums[r]]+=1

            while len(count) > k:
                count[nums[l_close]]-=1
                if count[nums[l_close]]==0:
                    del count[nums[l_close]]
                l_close+=1
                l_far=l_close

            # decrease the count of the left most element
            while count[nums[l_far]] > 1:
                count[nums[l_far]]-=1
                l_far+=1

            if len(count)==k:
                res+=l_far-l_close+1

        return res

print(Solution().subarraysWithKDistinct([1,2,1,2,3],2))