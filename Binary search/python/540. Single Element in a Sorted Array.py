"""You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
"""


class Solution:
    def singleNonDuplicate(self, nums) -> int:

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left+(right-left)//2

            left_mid = nums[mid-1] if mid-1 >= 0 else None

            right_mid = nums[mid+1] 

            if left_mid != nums[mid] and right_mid != nums[mid]:
                # if both sides are not equal to mid, then mid is the single element
                # [1,1,2,3,3,4,4]  1 - 2 - 3 here 2 is the single element
                # 2-3-3 here left side is different
                return nums[mid]  # found the single element



