

"""You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 

Constraints:

2 <= nums.length <= 105
"""


class Solution:
    def countSubarrays(self, nums, minK: int, maxK: int) -> int:

        left_bound = -1 # left bound of the current subarray
        lastMin, lastMax = -1, -1 # last index of minK and maxK

        count = 0

        for i in range(len(nums)):
            if nums[i] >= minK and nums[i] <= maxK:
                lastMin = i if nums[i] == minK else lastMin # update lastMin
                lastMax = i if nums[i] == maxK else lastMax # update lastMax

                count += max(0, min(lastMin, lastMax)-left_bound)
                # the number of subarrays that ends at i is the number of subarrays that ends at lastMin or lastMax

            else:
                left_bound = i
                lastMin, lastMax = -1, -1
   
        return count


if __name__ == "__main__":
    print(Solution().countSubarrays([1, 3, 5, 2, 7, 5], 1, 5))
 