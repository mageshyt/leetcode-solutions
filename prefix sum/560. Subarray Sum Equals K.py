'''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
'''

import collections


class Solution:
    def subarraySum(self, nums, k: int) -> int:

        hash_map = collections.defaultdict(int)

        hash_map[0] = 1

        prefix_sum = 0  # 0 % k will be 0

        res = 0

        for num in nums:
            # add to prefix sum
            prefix_sum += num

            # remainder of the prefix sum


if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 3
    print(Solution().subarraySum(nums, k))
