"""
You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. 

For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.
 
Example 1:

Input: nums = [4,4,4,5,6]
Output: true
Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.

"""

from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        cache={}

        def dfs(i):
            if i== len(nums):
                return True
            
            if i in cache:
                return cache[i]
            res=False
            # out of bounds case and for 2 same element
            if i < len(nums)-1 and nums[i]==nums[i+1]:
                res=dfs(i+2)

            # out of bounds case and for 3 same element
            if i < len(nums)-2 :
                # The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
                if nums[i]==nums[i+1] + nums[i+2]:
                    res =dfs(i+3)
                # The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. 
                if nums[i]+1==nums[i+1]== nums[i+2]-1:

                    res= res or dfs(i+3)


            cache[i]=res
        
            return cache[i]
 
        return dfs(0)




if __name__ == "__main__":
    
    
       print(Solution().validPartition([4,4,4,5,6]))
    
    
    