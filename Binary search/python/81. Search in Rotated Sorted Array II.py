"""There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        # base case

        if not nums:
            return False
        

        # binary search

        left=0
        right=len(nums)-1


        # perform binary search

        while left <=right:
            # find the mid
            mid=left+(right-left)//2
            
            mid_element=nums[mid]

            # if mid element is equal to target
            if mid_element==target:
                return True
            
            # now check the mid element with left if the are equal then we have to move left by one

            if mid_element==nums[left]:
                left+=1
                continue

            # if they are not equal then we can perform the binary search what we did in the previous problem

            # now check if we are in left sorted array or right sorted array

            if nums[left]<=mid_element:
                # we are in left sorted array now check if target is in left sorted array or not
                # if so then we have to move right to mid-1 else we have to move left to mid+1
                if nums[left]<=target<mid_element:
                    right=mid-1
                else:
                    left=mid+1
            else:
                # we are in right sorted array now check if target is in right sorted array or not
                # if so then we have to move left to mid+1 else we have to move right to mid-1
                if mid_element<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1

        return False
    
# Time complexity: O(logn)
# Space complexity: O(1)
