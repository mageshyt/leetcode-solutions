"""
You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
Add the value of the chosen integer to score.
Mark the chosen element and its two adjacent elements if they exist.
Repeat until all the array elements are marked.
Return the score you get after applying the above algorithm.

 

Example 1:

Input: nums = [2,1,3,4,5,2]
Output: 7
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
- 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
Our score is 1 + 2 + 4 = 7.
"""

from typing import List
import heapq

class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        n=len(nums)

        min_heap=[(nums[i],i) for i in range(n)]


        heapq.heapify(min_heap) # convert the list into a heap

        while min_heap:
            num,idx=heapq.heappop(min_heap)

            # if the num is not processed
            if nums[idx]!=-1:
                score+=num

                # mark it has processed
                nums[idx]=-1

                if idx>0 and nums[idx-1]!=-1:
                    nums[idx-1]=-1 # mark left element

                if idx<n-1 and nums[idx+1]!=-1:
                    nums[idx+1]=-1

        return score

nums = [2,3,5,1,3,2]

print(Solution().findScore(nums))
