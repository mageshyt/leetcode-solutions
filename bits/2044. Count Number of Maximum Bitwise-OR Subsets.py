"""
Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

 

Example 1:

Input: nums = [3,1]
Output: 2
Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]
Example 2:

Input: nums = [2,2,2]
Output: 7
Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.
Example 3:

Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
 

Constraints:

1 <= nums.length <= 16
1 <= nums[i] <= 105
"""

from typing import List
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # find the max_or
        max_or = 0
        for num in nums:
            max_or |= num

        memo = {}

        def dfs(i, cur_or):
            # base case
            if i==len(nums):
                return 1 if cur_or == max_or else 0

            if (i, cur_or) in memo:
                return memo[(i, cur_or)]


            # choice 1: pick the number
            pick = dfs(i+1, cur_or | nums[i])

            # choice 2: not pick the number
            not_pick = dfs(i+1, cur_or)

            memo[(i, cur_or)] = pick + not_pick


            return memo[(i, cur_or)]


        return dfs(0, 0)

# Time complexity: O(2^n)
# Space complexity: O(n)

print(Solution().countMaxOrSubsets([3,1])) # 2

