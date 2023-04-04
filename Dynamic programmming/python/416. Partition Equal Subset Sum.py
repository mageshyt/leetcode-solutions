"""Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


"""


class Solution:
    def canPartition(self, nums: list) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        dp = set()
        # add 0 and last element
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            for num in list(dp):
                dp.add(num + nums[i])
                if target in dp:
                    return True

        return False


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    print(Solution().canPartition(nums))
