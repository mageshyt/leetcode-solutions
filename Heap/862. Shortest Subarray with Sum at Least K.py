"""Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
"""
from typing import List
import heapq
from collections import deque
class Solution:
    # Time: O(n log n) |  Space: O(n)
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res=float('inf')

        heap=[] # (prefix_sum,end_idx)
        cur_sum=0

        for r in range(len(nums)):
            cur_sum+=nums[r]

            # consider possible res

            if cur_sum>=k:
                res=min(res,r+1)

            # min window ending at r

            while heap and cur_sum- heap[0][0]  >=k:
                _ , end_idx = heapq.heappop(heap)
                res=min(res,r-end_idx)

            # add current prefix_sum to heap
            heapq.heappush(heap,(cur_sum,r))

                

        return res == float('inf') and -1 or res

    # T
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        res=float('inf')
        q=deque()
        cur_sum=0

        for r in range(len(nums)):
            cur_sum+=nums[r]

            if cur_sum>=k:
                res=min(res,r+1)

            # min valid window ending at r
            while q and cur_sum- q[0][0] >=k:
                _, end_idx = q.popleft()
                res=min(res,r-end_idx)

            # validate monotonicity 
            while q and q[-1][0]>=cur_sum:
                q.pop()

            q.append((cur_sum,r))




        return res == float('inf') and -1 or res
 
if __name__ == "__main__":
    s= Solution()
    print(s.shortestSubarray([1],1))
    print(s.shortestSubarray([1,2],4))
    print(s.shortestSubarray([2,-1,2],3))

