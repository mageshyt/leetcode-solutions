'''Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.'''


class Solution:
    def canPartition(self, nums: list) -> bool:

        # if sum is not even then return false because we cant partition it
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums)//2
        # sort the inputs
        nums.sort()

        count_up = 0

        temp = nums.copy()
        for i, num in enumerate(nums):

            if count_up == target:
                break
            else:
                count_up += num
                # pop the num
                temp.pop(0)

        return count_up == target and sum(temp) == target


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 5]
    print(s.canPartition(nums))
