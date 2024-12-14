"""
You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [5,4,2,4]
Output: 8
Explanation: 
Continuous subarray of size 1: [5], [4], [2], [4].
Continuous subarray of size 2: [5,4], [4,2], [2,4].
Continuous subarray of size 3: [4,2,4].
Thereare no subarrys of size 4.
Total continuous subarrays = 4 + 3 + 1 = 8.
It can be shown that there are no more continuous subarra
"""

from typing import List
import heapq
class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        minHeap=[] # (num,index)
        maxHeap=[] # (-num,index)

        left=right=0

        res =0

        while right < n :
            heapq.heappush(minHeap,(nums[right],right))
            heapq.heappush(maxHeap,(-nums[right],right))

            # shrink window
            while left < right and -maxHeap[0][0] - minHeap[0][0] > 2:
                left+=1

                # remove the outside elements

                while minHeap and minHeap[0][1] < left:
                    heapq.heappop(minHeap)

                while maxHeap and maxHeap[0][1] < left:
                    heapq.heappop(maxHeap)


            res+=right-left+1
            right+=1
        return res



nums = [5,4,2,4]
print(Solution().continuousSubarrays(nums))
