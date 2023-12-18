"""The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

 

Example 1:

Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
"""

from typing import List
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        return self.helper(nums)



    
    def helper(self,nums: List[int]) -> int:

        max_num = [max(nums[0],nums[1]),min(nums[0],nums[1])]
        min_num= [min(nums[0],nums[1]),max(nums[0],nums[1])]

        for i in range(2,len(nums)):
            curr= nums[i]

            max_1,max_2 = max_num

            if curr > max_1:
                max_num = [curr,max_1]
            elif curr > max_2:
                max_num = [max_1,curr]
            min_1,min_2 = min_num

            if curr < min_1:
                min_num = [curr,min_1]
            elif curr < min_2:
                min_num = [min_1,curr]


            print(max_num,min_num)

        return max_num[0]*max_num[1]-min_num[0]*min_num[1]


if __name__ == "__main__":
    nums = [4,2,5,9,7,4,8]

    print(Solution().maxProductDifference(nums))

