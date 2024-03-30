"""You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times."""
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res=0
        n=len(nums)
        max_n,max_cnt=max(nums),0 # max val count in the subarray
        l=0
        for r in range(n):
            # if we found the max count increase the count
            if nums[r]==max_n:
                max_cnt+=1

            while max_cnt > k or (l <=r and max_cnt==k and nums[l] !=max_n):
                if nums[l]==max_n:
                    max_cnt-=1
                l+=1
            if max_cnt == k:
                res+=l+1
        return res
 
    

