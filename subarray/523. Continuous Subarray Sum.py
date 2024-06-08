"""
523. Continuous Subarray Sum
Solved
Medium
Topics
Companies
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.


Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false

"""
from typing import List
from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders=defaultdict(int)
        # Base case
        if len(nums)<2:
            return False

        # set the first element to 0
        remainders[0]=-1
        sum=0

        for i in range(len(nums)):
            # add the current element to the sum
            sum+=nums[i]

            # if k is not 0, then take the remainder of the sum
            if k!=0:
                sum%=k

            # if the remainder is already in the dictionary, then the subarray sum is a multiple of k
            if remainders.get(sum)!=None:
                # check the length of the subarray
                size=i-remainders[sum]
                if size>1:
                    return True

            # if the remainder is not in the dictionary, then add it
            else:
                remainders[sum]=i

        return False
