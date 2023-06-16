"""Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:


Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.
Example 2:


Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]
Example 3:


Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST."""
from math import comb
from typing import List


class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        mod = 10**9+7

        n = len(nums)

        def helper(nums):
            if len(nums) <= 2:
                return 1
            parent = nums[0]
            # left is the list of numbers smaller than parent
            left = [num for num in nums if num < parent]
            # right is the list of numbers larger than parent
            right = [num for num in nums if num > parent]
            print(left, right)
            # left_res is the number of ways to reorder left
            left_res = helper(left) % mod

            # right_res is the number of ways to reorder right
            right_res = helper(right) % mod

            # comb(len(left)+len(right),len(left)) is the number of ways to reorder left+right
            return comb(len(left)+len(right), len(left)) * left_res * right_res % mod

        # -1 because we don't count the original array
        return (helper(nums)-1) % mod


print(Solution().numOfWays([2, 1, 3]))
