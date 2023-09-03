"""
You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.

For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
Return the minimum number of operations to make an array that is sorted in non-decreasing order.

 

Example 1:

Input: nums = [3,9,3]
Output: 2
Explanation: Here are the steps to sort the array in non-decreasing order:
- From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
- From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.
"""
from typing import List
from typing import List
import math

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0  # Initialize a variable to store the result, i.e., the minimum number of replacements.
        maxMin = nums[-1]  # Initialize a variable to store the maximum minimum value, starting from the last element.

        # Loop through the list in reverse order, skipping the last element.
        for num in reversed(nums[:-1]):
            parts = math.ceil(num / int(maxMin))  # Calculate the number of parts needed for the current element using ceiling division.

            res += (parts - 1)  # Increment the result by parts - 1, as that's the number of replacements required.

            maxMin = num / parts  # Update the maximum minimum value using the formula num / parts.

        return res  # Return the minimum number of replacements required.


print(Solution().minimumReplacement([1,13,15,2,5,14,12,17]))