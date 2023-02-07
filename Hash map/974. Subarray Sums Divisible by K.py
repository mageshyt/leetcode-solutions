'''Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0'''

import collections


class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:

        # res
        res = 0

        # hash map to store the remainder
        hash_map = collections.defaultdict(int)
        hash_map[0] = 1

        prefix_sum = 0
        for i, num in enumerate(nums):
            # add the current number to the prefix sum
            prefix_sum += num

            # remainder of the prefix sum
            remainder = prefix_sum % k

            res += hash_map[remainder]

            hash_map[remainder] += 1  # add the remainder to the hash map

        return res


if __name__ == "__main__":
    nums = [4, 5, 0, -2, -3, 1]
    k = 5
    print(Solution().subarraysDivByK(nums, k))
