"""A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.
Example 1:

Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
Output: [true,false,true]
Explanation:
In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an arithmetic sequence.
"""

from typing import List
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        # 1. create a list to store the result
        result = []

        # 2. iterate through the l and r arrays
        for i in range(len(l)):
            left, right = l[i], r[i]
            # 3. slice the nums array
            subarray = nums[left:right+1]
            # 4. append the result of the helper function to the result list
            result.append(self.helper(subarray))
        
        # 5. return the result list
        return result

    
    def helper(self,nums):

        # 1 . sort the array
        nums.sort()

        # 2. check if the difference between every two consecutive elements is the same

        diff = nums[1] - nums[0]

        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] != diff:
                return False
            
        return True
    
