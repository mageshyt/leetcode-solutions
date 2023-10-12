"""You are given an integer array nums. In one operation, you can replace any element in nums with any integer.

nums is considered continuous if both of the following conditions are fulfilled:

All elements in nums are unique.
The difference between the maximum element and the minimum element in nums equals nums.length - 1.
For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

Return the minimum number of operations to make nums continuous.

 

Example 1:

Input: nums = [4,2,5,3]
Output: 0
Explanation: nums is already continuous.
Example 2:

Input: nums = [1,2,3,5,6]
Output: 1
Explanation: One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.
"""

from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums) # size of the array
        # step 1: we are going to remove the duplicates and sort the array

        nums=sorted(set(nums)) # sorted the array and remove the duplicates

        # step 2: we are going to find the longest subarray with consecutive elements
        res=n # the maximum length of the subarray is n

        right=0 # left pointer

        for left in range(n):

            # our range will be nums[left] to nums[left]+len(nums)-1

            while ( right < n )and  nums[right] < nums[left]+ n: # if the length of the subarray is greater than the length of the array
                right+=1 # we move the right pointer to the right

            window_size=right-left # the length of the subarray
            # Reason for n-window_size: the remaining elements are the ones we need to replace
            res=min(res,n-window_size) # we update the result



        return res
    
# Time complexity: O(nlogn)
# Space complexity: O(n)


