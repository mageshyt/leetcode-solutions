
"""Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20]."""

from typing import List
import heapq
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        heap=[(-nums[0],0)] # (sum,index)

        ans=nums[0]

        for i in range (1,len(nums)):

            # if the index of the top of the heap is out of range, pop it
            # heap[0][1] is the index of the top of the heap    
            while heap and heap[0][1] < i-k:

                heapq.heappop(heap)

            curr=max(0,-heap[0][0])+nums[i] # calculate the current sum

            ans=max(ans,curr) # update the answer

            heapq.heappush(heap,(-curr,i)) # push the sum and index

        return ans
    
# Time complexity: O(nlogk)
# Space complexity: O(k)

if __name__ == "__main__":
    nums = [10,2,-10,5,20]
    k = 2
    print(Solution().constrainedSubsetSum(nums,k)) # 37