"""You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

 

Example 1:

Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
"""
from typing import List
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum=sum(nums) # sum of all elements in nums

        res=[]
        leftSum=0 # sum of all elements to the left of i

        for i in range(len(nums)):
            # right sum will be total sum - left sum - nums[i]
            rightSum=total_sum-leftSum-nums[i]

            # now find the left size & right size

            leftSize=i
            rightSize=len(nums)-i-1

            # now find the sum of absolute difference

            res.append(
                leftSize*nums[i]-leftSum+rightSum-rightSize*nums[i]
            )

            # update left sum

            leftSum+=nums[i]

        return res


# Time Complexity: O(N)
# Space Complexity: O(N)

if __name__ == "__main__":
    nums = [2,3,5]
    print(Solution().getSumAbsoluteDifferences(nums))