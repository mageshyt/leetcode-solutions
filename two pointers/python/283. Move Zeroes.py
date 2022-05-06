'''Given an integer array nums, move all 0's
 to the end of it while maintaining the relative order of the non-zero
  elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''

from operator import le


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=0
        while left<len(nums):
            if(nums[left]!=0):
                nums[right]=nums[left]
                right+=1
            left+=1
        while right<len(nums):
            nums[right]=0
            right+=1
        return nums
test=Solution()
print(test.moveZeroes([0,1,0,3,12]))

        