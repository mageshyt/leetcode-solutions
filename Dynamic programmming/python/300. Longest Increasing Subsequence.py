"""Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4."""
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Dictionary to store computed results
        dp = {}

        def dfs(i, j, count=0):
            # Base case: If all elements are processed, return the count
            if i == len(nums):
                return count

            # Check if the result is already computed and return it
            if (i, j) in dp:
                return dp[(i, j)]

            # Logic:
            # If the current element is greater than the previous element, we have two choices:
            # 1. Include the current element in the increasing subsequence
            # 2. Skip the current element and continue with the previous count

            # If the current element is greater, explore both choices
            if nums[i] > j:
                # Choice 1: Include the current element and increment the count
                include_count = dfs(i + 1, nums[i], count + 1)

                # Choice 2: Skip the current element and continue with the previous count
                skip_count = dfs(i + 1, j, count)

                # Take the maximum of the two choices
                dp[(i, j)] = max(include_count, skip_count)
            else:
                # If the current element is not greater, skip it and continue with the previous count
                dp[(i, j)] = dfs(i + 1, j, count)

            # Return the computed result
            return dp[(i, j)]

        # Start the recursive process with the initial index 0 and previous element set to negative infinity
        return dfs(0, float('-inf'))

    # bottom up sol

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)

        return max(dp)


nums = [10,9,2,5,3,7,101,18]

print(Solution().lengthOfLIS(nums))



