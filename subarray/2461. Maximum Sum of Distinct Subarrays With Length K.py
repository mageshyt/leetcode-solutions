"""You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
 

Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
"""

from typing import List
from collections import defaultdict 
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        window_sum = 0
        count=defaultdict(int)

        l=0

        for r in range(len(nums)):
            window_sum+=nums[r]
            count[nums[r]]+=1

            if r-l+1==k:
                # if we have k distinct elements
                if len(count)==k:
                    max_sum=max(max_sum,window_sum)

                # remove the left element
                window_sum-=nums[l]
                count[nums[l]]-=1
                # if the count of the left element is 0, remove it from the dictionary
                if count[nums[l]]==0:
                    del count[nums[l]]

                l+=1

        return max_sum

if __name__ == "__main__":
    s = Solution()
    print(s.maximumSubarraySum([1,5,4,2,9,9,9], 3))
    print(s.maximumSubarraySum([4,4,4], 3))


