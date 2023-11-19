"""Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal.

 

Example 1:

Input: nums = [5,1,3]
Output: 3
Explanation: It takes 3 operations to make all elements in nums equal:
1. largest = 5 at index 0. nextLargest = 3. Reduce nums[0] to 3. nums = [3,1,3].
2. largest = 3 at index 0. nextLargest = 1. Reduce nums[0] to 1. nums = [1,1,3].
3. largest = 3 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,1].
Example 2:

Input: nums = [1,1,1]
Output: 0
Explanation: All elements in nums are already equal."""

from typing import List
from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        hash_table = Counter(nums)
        # 1. sort the array

        print(hash_table)


        # remove the duplicates
        nums=list(set(nums))

        # nums=list(set(nums))
        nums.sort(key=lambda x: -x)

        smallest = nums[-1]
        print(nums)
        # remove the 
        res = 0

        for i in range(len(nums)):
            #find the unique elements
            if nums[i] == smallest:
                continue
            # print(">> remianing elements", len(nums)-i-1)
            res += hash_table[nums[i]] * (len(nums)-i-1)
            # print(res

        return res

if __name__ == "__main__":
    nums =[1,1,2,2,3]
    sol = Solution()
    print(sol.reductionOperations(nums))
