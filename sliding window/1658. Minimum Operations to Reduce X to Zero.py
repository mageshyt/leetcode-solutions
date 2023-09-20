"""You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
"""
from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # find the longest subarray with sum equal to sum(nums)-x

        target=sum(nums)-x

        if target==0:
            return len(nums)
        
        if target<0:
            return -1
        
        left=0 #  left pointer [window start]
        right=0 # right pointer [window end]

        max_len=-1 # max len of subarray with sum equal to target

        cur_sum=0 # current sum of subarray

        while right <len(nums):
            # add the right element to the current sum
            cur_sum+=nums[right]
            # move right pointer

            right+=1

            # if the current sum is greater than the target, then move the left pointer

            while(right <= len(nums) and cur_sum>target):
                cur_sum-=nums[left]
                left+=1

            # if the current sum is equal to the target, then update the max length
            if cur_sum==target:
                max_len=max(max_len,right-left)

        
        return len(nums)-max_len if max_len!=-1 else -1
      



        