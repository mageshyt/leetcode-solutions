"""
You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.

 

Example 1:

Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.

"""

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        mask=0
        max1=0
        i=0 # left
        for j in range(len(nums)):  #right
            while((mask & nums[j])!=0):
                mask^=nums[i]  
                i+=1
            mask |=nums[j]
            max1=max(max1,j-i+1)
        
        return max1

print(Solution().longestNiceSubarray([1,3,8,48,10]))
