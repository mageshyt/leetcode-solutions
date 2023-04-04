"""Given an integer array nums, find a
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray."""


class Solution:
    def maxProduct(self, nums) -> int:
        res: int = nums[0]
        max_product: int = nums[0]  # max product so far
        min_product: int = nums[0]  # min product so far

        for i in range(1, len(nums)):
            temp = max_product
            curr = nums[i]

            max_product = max(
                curr, max(curr * max_product, curr * min_product))

            min_product = min(
                curr, min(curr * temp, curr * min_product))
            res = max(res, max_product)

        return res


if __name__ == "__main__":
    nums = [2, 3, -2, 4]

    print(Solution().maxProduct(nums))
