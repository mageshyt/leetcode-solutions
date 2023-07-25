"""Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5."""

from typing import List



class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # Initialize an array dp with 1s to store the length of the longest increasing subsequence ending at each index.
        dp = [1] * len(nums)

        # Initialize an array count with 1s to store the count of longest increasing subsequences ending at each index.
        count = [1] * len(nums)

        # Initialize a variable _max to store the length of the longest increasing subsequence found so far.
        _max = 1

        # Loop through the input array starting from index 1.
        for i in range(1, len(nums)):
            # Compare the current element with all previous elements (j) up to i.
            for j in range(0, i):
                # If the current element is greater than the previous element, it can be part of an increasing subsequence.
                if nums[i] > nums[j]:
                    # If the length of the increasing subsequence ending at i is less than (dp[j] + 1) where dp[j] is the length
                    # of the longest increasing subsequence ending at j, update dp[i] and count[i].
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    # If the length of the increasing subsequence ending at i is equal to (dp[j] + 1), increment count[i]
                    # as we have found another way to get the same length of increasing subsequence.
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]

            # Update _max with the maximum length of the increasing subsequence found so far.
            _max = max(_max, dp[i])

        # Sum up the counts of longest increasing subsequences whose length is equal to _max.
        return sum([count[i] for i in range(len(nums)) if dp[i] == _max])

    

sol=Solution()

nums=[1,3,5,4,7]
print(sol.findNumberOfLIS(nums))
